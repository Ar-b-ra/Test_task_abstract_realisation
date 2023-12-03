import os

from external_storage.kafka_storage import KafkaStorage
from external_storage.postgres_broker import PostgresStorage

if __name__ == "__main__":
    storage_type = os.environ.get("PLACE_TO_SEND", "postgres")  # or kafka
    agr_time = os.environ.get("AGR_TIME")  # time from env
    url = os.environ.get("URL")
    if storage_type == "postgres":
        login = input("Enter login: ")
        password = input("Enter password: ")
        storage = PostgresStorage(url=url, login=login, password=password)
    else:
        storage = KafkaStorage(url=url)


