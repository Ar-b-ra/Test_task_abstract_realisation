# Используем базовый образ Python
FROM python:latest
LABEL authors="Роман"
COPY requirements.txt .

RUN apt update -y && \
    apt upgrade -y && \
    apt install -y --no-install-recommends \
        git && \
        python3-pip && \
    apt autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Ar-b-ra/Test_task_abstract_realisation.git
# Установка рабочей директории
WORKDIR /Test_task_abstract_realisation

RUN pip install --upgrade pip && \
    pip install -r requirements.txt \
ENV STORAGE_TYPE=posgres

CMD [ "python3", "main.py" ]