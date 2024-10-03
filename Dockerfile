# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем файлы зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY start.sh .
RUN chmod a+x start.sh && chown appuser:appuser start.sh

# Копируем файлы проекта в текущую директорию контейнера
COPY . .

# Определяем порт, который контейнер будет слушать
EXPOSE 8088

ENTRYPOINT ["/start.sh"]
