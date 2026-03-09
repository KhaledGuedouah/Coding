FROM python:3.12-slim

WORKDIR /app

# No external deps needed; keep image small.
COPY app.py /app/app.py

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "/app/app.py"]
