# Library
# Описание
__Библиотека, хранилище книг.__
## Функционал

* Пользователи могут создавать книги
* Пользователи могут просматривать список книг
* Пользователи могут просматривать детальную информацию по любой книге
* Пользователи могут изменять информацию по своим книгам
* Пользователи могут удалять свои книги

## Права доступа

Доступ ко всем эндпоитам имеют только авторизованные пользователи.

## Подготовка и запуск проекта
#### Клонирование репозитория
Склонируйте репозиторий на локальную машину:
```bash
git clone https://github.com/Slavchick12/library.git
```
#### Подготовка базы данных PostgreSQL
##### Шаг 1. Скачайте и установите PostreSQL 14.5
```
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
```
##### Шаг 2. Запустите PostgreSQL и создайте БД с любым названием
#### Подготовка секретных переменных
##### Шаг 1. Перейдите в директорию с проектом backend
```bash
cd <path_to_project>/backend/
```
##### Шаг 2. Создайте файл *.env*
##### Шаг 3. Заполните *.env* следующем образом
```
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=<DB_NAME, str>
DB_USER=<DB_USER, str>
DB_PASSWORD=<DB_PASSWORD, str>
DB_HOST=127.0.0.1
DB_PORT=5432
SECRET_KEY=<DJANGO_SECRET_KEY>
DEBUG=<True/False>
TOKEN_LIFETIME_DAYS=<TOKEN_LIFETIME_DAYS, int>
```
#### Настройка виртуального окружения и проведение миграций
##### Шаг 1. Установка виртуального окружения
```bash
cd <path_to_project>/backend/
```
```bash
python -m venv venv
```
##### Шаг 2. Активация виртуального окружения
```bash
. venv/Scripts/activate
```
##### Шаг 3. Обновление пакетов pip
```bash
python -m pip install -U pip
```
##### Шаг 4. Установка зависимостей проекта
```bash
pip install -r requirements.txt
```
##### Шаг 5. Проведение миграции
Убедитесь, что Вы находитесь в директории с файлом manage.py и выполните команду
```bash
python manage.py migrate
```
#### Запуск проекта на локальной машине
```bash
python manage.py runserver
```
#### Создание суперюзера
```bash
python manage.py createsuperuser
```
#### Админ-панель Django
```bash
http://127.0.0.1:8000/admin
```
## JWT-авторизация
##### Шаг 1. Создание пользователя. Отправьте POST-запрос на адрес:
```
http://127.0.0.1:8000/auth/users/
```
##### Шаг 2. Получение токена авторизации. Отправьте POST-запрос на адрес и получите токен **access**:
```
http://127.0.0.1:8000/auth/jwt/create/
```
##### Шаг 3. Использование токена. При отправке запроса, вставьте полученный токен в параметр Authorization с ключом **Bearer**:
```
Authorization: Bearer <access-token>
```
## Используемый стек
```
Python, Django, DRF, PostgreSQL, Simple-JWT
```
#### Также используется
```
flake8, isort, psycopg2-binary
```
