from external_storage.abstract_storage import AbstractStorage
from va_bas import Event


class PostgresStorage(AbstractStorage):

    def __init__(self, url, *, login: str, password: str):
        super().__init__(url="localhost:1234")
        self.login = login
        self.password = password

    def connect(self):
        print(f"Connected to {self.url} with login = {self.login} and password = {self.password}")

    def send_aggregated_events(self, event: Event):
        print(f"Send {event = } to postgres")
