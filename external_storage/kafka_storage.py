from kafka import KafkaConsumer, KafkaProducer

from external_storage.abstract_storage import AbstractStorage


class KafkaStorage(AbstractStorage):

    def __init__(self, url: str):
        super().__init__(url="localhost:1234")
        self.consumer = KafkaConsumer('my_favorite_topic')
        self.producer = KafkaProducer(bootstrap_servers='localhost:1234')
