#!/usr/bin/env python3
"""
Open-Meteo CLI: fetch current weather and cache responses.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict
from urllib.parse import urlencode
from urllib.request import urlopen


API_URL = "https://api.open-meteo.com/v1/forecast"
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
DEFAULT_CACHE_TTL = 30 * 60  # 30 minutes


@dataclass(frozen=True)
class Location:
    name: str
    latitude: float
    longitude: float


def read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def fetch_json(url: str, params: Dict[str, Any]) -> Dict[str, Any]:
    query = urlencode(params)
    with urlopen(f"{url}?{query}") as resp:
        return json.loads(resp.read().decode("utf-8"))


def geocode_city(city: str) -> Location:
    data = fetch_json(GEOCODE_URL, {"name": city, "count": 1, "language": "en", "format": "json"})
    results = data.get("results") or []
    if not results:
        raise ValueError(f"City not found: {city}")
    r0 = results[0]
    return Location(name=r0["name"], latitude=r0["latitude"], longitude=r0["longitude"])


def weather_key(lat: float, lon: float, units: str) -> str:
    return f"{lat:.4f},{lon:.4f}|{units}"


def get_cached_weather(cache: Dict[str, Any], key: str, ttl: int) -> Dict[str, Any] | None:
    entry = cache.get(key)
    if not entry:
        return None
    if time.time() - entry.get("timestamp", 0) > ttl:
        return None
    return entry.get("data")


def set_cached_weather(cache: Dict[str, Any], key: str, data: Dict[str, Any]) -> None:
    cache[key] = {"timestamp": int(time.time()), "data": data}


def fetch_weather(lat: float, lon: float, units: str) -> Dict[str, Any]:
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "temperature_unit": "fahrenheit" if units == "us" else "celsius",
        "windspeed_unit": "mph" if units == "us" else "kmh",
        "precipitation_unit": "inch" if units == "us" else "mm",
        "timezone": "auto",
    }
    return fetch_json(API_URL, params)


def format_output(location: str, data: Dict[str, Any], units: str) -> str:
    current = data.get("current_weather") or {}
    temp = current.get("temperature")
    wind = current.get("windspeed")
    wdir = current.get("winddirection")
    time_str = current.get("time")
    temp_unit = "F" if units == "us" else "C"
    wind_unit = "mph" if units == "us" else "km/h"
    return (
        f"{location}\n"
        f"Time: {time_str}\n"
        f"Temperature: {temp} °{temp_unit}\n"
        f"Wind: {wind} {wind_unit} @ {wdir}°\n"
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Get current weather from Open-Meteo.")
    p.add_argument("--city", help="City name for geocoding (e.g., Paris)")
    p.add_argument("--lat", type=float, help="Latitude")
    p.add_argument("--lon", type=float, help="Longitude")
    p.add_argument("--units", choices=["metric", "us"], default="metric", help="Units system")
    p.add_argument("--cache", default=str(Path(".cache") / "weather.json"), help="Cache file path")
    p.add_argument("--ttl", type=int, default=DEFAULT_CACHE_TTL, help="Cache TTL in seconds")
    return p


def resolve_location(args: argparse.Namespace) -> Location:
    if args.city:
        return geocode_city(args.city)
    if args.lat is not None and args.lon is not None:
        return Location(name=f"{args.lat},{args.lon}", latitude=args.lat, longitude=args.lon)
    raise ValueError("Provide --city or both --lat and --lon.")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        location = resolve_location(args)
        cache_path = Path(args.cache)
        cache = read_json(cache_path)
        
        key = weather_key(location.latitude, location.longitude, args.units)

        data = get_cached_weather(cache, key, args.ttl)
        if data is None:
            data = fetch_weather(location.latitude, location.longitude, args.units)
            set_cached_weather(cache, key, data)
            write_json(cache_path, cache)

        print(format_output(location.name, data, args.units))
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
