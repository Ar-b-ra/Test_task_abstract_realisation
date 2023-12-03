from kafka import KafkaConsumer, KafkaProducer

from where_to_save.base_send_place import BaseBroker


class KafkaBroker(BaseBroker):

    def __init__(self):
        super().__init__(url="localhost:1234")
        self.consumer = KafkaConsumer('my_favorite_topic')
        self.producer = KafkaProducer(bootstrap_servers='localhost:1234')
