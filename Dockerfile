FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

# Create a non-root user for security
RUN useradd -m appuser && mkdir -p /var/log/app && chown -R appuser /app /var/log/app
USER appuser

CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port 8000 2>&1 | tee /var/log/app/fastapi.log"]
