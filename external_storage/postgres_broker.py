from aggregator import AggEvent
from external_storage.abstract_storage import AbstractStorage


class PostgresStorage(AbstractStorage):

    def __init__(self, url, *, login: str, password: str):
        super().__init__(url="localhost:1234")
        self.login = login
        self.password = password

    def connect(self):
        print(f"Connected to {self.url} with login = {self.login} and password = {self.password}")

    async def send_aggregated_events(self, event: AggEvent):
        print(f"Send {event = } to postgres")

    def disconnect(self):
        print("Disconnected from Postgres")