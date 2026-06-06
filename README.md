# Kittygram

Социальная сеть для публикации фотографий котиков и их достижений.

## Стек технологий

- Python 3.11, Django 5.2, Django REST Framework
- React
- Nginx, Gunicorn
- Docker, Docker Compose

## Запуск проекта

### 1. Клонировать репозиторий
```bash
git clone https://github.com/vasilievakira2006-oss/kittygram_backend1.git
cd kittygram_backend1
```

### 2. Создать `.env`
```bash
cp .env.example .env
```
Заполнить `.env`:
### 3. Запустить
```bash
docker compose up -d --build
docker compose exec backend python manage.py migrate
```

### 4. Открыть в браузере

| Адрес | Описание |
|---|---|
| http://localhost | Сайт |
| http://localhost/admin/ | Админка |
| http://localhost/api/ | API |

## Автор

[Кира Васильева](https://github.com/vasilievakira2006-oss)