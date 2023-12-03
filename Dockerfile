# Используем базовый образ Python
FROM python:latest
LABEL authors="Роман"
COPY requirements.txt .

RUN apt update -y && \
    apt upgrade -y && \
    apt install -y --no-install-recommends \
        git && \
    apt autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python3", "main.py" ]