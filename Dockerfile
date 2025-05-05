
FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir edge-tts fastapi uvicorn

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
