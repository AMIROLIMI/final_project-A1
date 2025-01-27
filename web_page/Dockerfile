# Используем официальный образ Python 3.12 slim (облегченный)
FROM python:3.12.3-slim

# Устанавливаем рабочую директорию контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY dependencies.txt .

# Устанавливаем зависимости из файла 
RUN pip install --no-cache-dir -r dependencies.txt

# Копируем весь проект в рабочую директорию
COPY . .

# Открываем порт 8000 для доступа к Flask-приложению
EXPOSE 8000

# Указываем команду для запуска приложения
CMD ["python", "web_page.py"]
