import os

from aggregator import Aggregator
from external_storage.kafka_storage import KafkaStorage
from external_storage.postgres_broker import PostgresStorage
from va_bas import VaBus, Event

if __name__ == "__main__":
    storage_type = os.environ.get("STORAGE_TYPE", "postgres")  # or kafka
    agr_time = os.environ.get("AGR_TIME")  # time from env (?)
    url = os.environ.get("URL")
    if storage_type == "postgres":
        login = input("Enter login: ")
        password = input("Enter password: ")
        storage = PostgresStorage(url=url, login=login, password=password)
    else:
        storage = KafkaStorage(url=url)
    bus = VaBus(url=url)
    with bus:
        aggregator = Aggregator(storage)
        storage.connect()
        event = bus.send_event(Event("event1", 1, 1))
        aggregator.add_event(Event("event2", 2, 2))
        aggregator.add_event(Event("event3", 3, 3))  # TODO: уточнить интерфес получения и отправки событий

        agg_event = aggregator.aggregate_events()
        storage.send_aggregated_events(agg_event)

