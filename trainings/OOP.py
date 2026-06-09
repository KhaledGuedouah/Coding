# Interview preparation practice module.
# Contains algorithms and data structure exercises for coding interviews.

from dataclasses import dataclass, field
from time import time
@dataclass
class Packet:
    src: int
    dst: int
    payload: bytes
    crc: int = 0
    tags: list[str] = field(default_factory=list)

p = Packet(1, 2, b"\x01\x02")
print(p)                  # repr auto
print(p == Packet(1,2,b"\x01\x02"))  # eq auto


########################### Sensor Sampling API #############################


@dataclass(frozen=True, slots=True)
class Sample:
    value: float
    timestamp: float

class SensorIO:
    """Interface/adapter for real HW; can be mocked in tests."""
    def read_raw(self) -> float:
        raise NotImplementedError

class Sensor:
    def __init__(self, io: SensorIO, scale: float = 1.0, offset: float = 0.0):
        self._io = io              # internal
        self._scale = scale
        self._offset = offset

    @property
    def scale(self) -> float:
        return self._scale

    @property
    def offset(self) -> float:
        return self._offset

    def calibrate(self, *, scale: float | None = None, offset: float | None = None) -> None:
        if scale is not None:
            if scale == 0:
                raise ValueError("scale must be non-zero")
            self._scale = scale
        if offset is not None:
            self._offset = offset

    def read(self) -> Sample:
        raw = self._io.read_raw()
        val = raw * self._scale + self._offset
        return Sample(val, time())

# Example "mock" I/O for tests
class FakeIO(SensorIO):
    def __init__(self, values):
        self._values = iter(values)
    def read_raw(self) -> float:
        return next(self._values)

io = FakeIO([10, 20, 30])
s = Sensor(io, scale=0.1, offset=1.0)
print(s.__dict__)
# print(s.read())  # Sample(value=2.0, timestamp=...)

