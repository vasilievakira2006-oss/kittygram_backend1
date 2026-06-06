FROM python:3.11-slim

WORKDIR /app

# Копируем и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код
COPY . .

# Собираем статику
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Gunicorn — продакшн сервер вместо runserver
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kittygram_backend.wsgi"]