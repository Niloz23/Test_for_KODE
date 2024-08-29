# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы проекта в рабочую директорию контейнера
COPY . /app

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install django djangorestframework requests django-cors-headers

# Выполняем миграции
RUN python manage.py makemigrations
RUN python manage.py migrate

# Открываем порт
EXPOSE 8000

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]