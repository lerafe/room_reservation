# FastAPI Room Reservation

## Описание проекта

Проект представляет собой API для приложения, которое предоставляет возможность бронировать помещения на определённый период времени.

## Основные модели

- **MeetingRoom**: Модель, описывающая переговорные комнаты.
- **Reservation**: Модель, описывающая бронирование (какая переговорка забронирована, кем и на какой период времени).
- **User**: Модель пользователей с разделением ролей на обычных пользователей и суперюзеров (администраторов) системы.

## Ключевые возможности

- Бронирование свободных переговорок на определённый период времени.
- Проверка доступности переговорок на запрашиваемое время.
- Управление пользователями и ролями (обычные пользователи и администраторы).

## Технологии, используемые в проекте

Проект построен с использованием следующих технологий:

- **FastAPI**: Современный, высокопроизводительный веб-фреймворк для построения API на Python 3.6+.
- **Uvicorn**: Быстрый ASGI-сервер для запуска приложений на основе ASGI.
- **SQLAlchemy**: Популярная ORM (Object-Relational Mapping) библиотека для работы с базами данных.
- **ФAync IO**: Модуль для поддержки асинхронного программирования в SQLAlchemy, что позволяет выполнять асинхронные запросы к базе данных.
- **Pydantic**: Библиотека для валидации данных и управления настройками на основе типов данных Python.


## API для проекта

API предоставляет следующие эндпоинты:

- **POST /meeting_rooms/** — создание новой переговорной комнаты (только для суперюзеров).
- **GET /meeting_rooms/** — получение списка всех переговорных комнат.
- **GET /meeting_rooms/{meeting_room_id}/reservations** — получение списка бронирований для конкретной переговорной комнаты.
- **POST /reservations/** — создание нового бронирования.
- **GET /reservations/** — получение списка всех бронирований.
- **PUT /reservations/{reservation_id}** — обновление существующего бронирования.
- **POST /auth/jwt/login** — авторизация пользователя.
- **POST /auth/register** — регистрация нового пользователя.
- **GET /users/** — получение списка всех пользователей.

# Как развернуть и запустить проект

Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/lerafe/room_reservation.git
```

```
cd room_reservation
```

Cоздайте и активируйте виртуальное окружение:

```
python3 -m venv venv
```

* Linux/macOS

    ```
    source venv/bin/activate
    ```

* Windows

    ```
    source venv/scripts/activate
    ```

Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

В кореной директории проекта создайте файл .env c содержимым:

```
APP_TITLE=Сервис бронирования переговорных комнат
APP_DESCRIPTION=Это описание проекта, загруженное из env-файла.
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=[ваш секретный код]
FIRST_SUPERUSER_EMAIL=[почта суперюзера]
FIRST_SUPERUSER_PASSWORD=[пароль суперюзера]
```

Создайте базу данных и первую миграцию:

```
alembic revision --autogenerate -m "First migration"
```

Выполните непримененную миграцию:
```
alembic upgrade head
```

Запуск проекта:
```
uvicorn main:app
```

## Лицензия
Этот проект лицензирован под MIT License.
