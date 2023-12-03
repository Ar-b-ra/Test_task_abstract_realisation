from kafka import KafkaConsumer, KafkaProducer

from aggregator import AggEvent
from external_storage.abstract_storage import AbstractStorage


class KafkaStorage(AbstractStorage):

    def __init__(self, url: str):
        super().__init__(url="localhost:1234")
        self.consumer = KafkaConsumer('my_favorite_topic')
        self.producer = KafkaProducer(bootstrap_servers='localhost:1234')

    def connect(self):
        print("Connected to Kafka")

    def disconnect(self):
        print("Disconnected from Kafka")

    async def send_aggregated_events(self, event: AggEvent):
        print(f"Send {event = } to kafka")
