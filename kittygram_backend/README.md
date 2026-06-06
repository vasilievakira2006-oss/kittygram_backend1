# Kittygram Backend

REST API для проекта Kittygram на Django.

## Установка и запуск локально

```bash
cd kittygram_backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Запуск через Docker

```bash
docker compose up -d --build
docker compose exec backend python manage.py migrate
```

## API эндпоинты

- `/api/cats/` — список котиков
- `/api/achievements/` — достижения
- `/admin/` — админка Django