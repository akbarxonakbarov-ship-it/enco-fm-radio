FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY .env.example ./.env.example

CMD ["uvicorn", "app.admin_bot.main:app", "--host", "0.0.0.0", "--port", "10000"]
