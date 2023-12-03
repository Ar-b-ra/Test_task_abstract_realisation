from abc import ABCMeta, abstractmethod

from aggregator import AggEvent


class AbstractStorage(metaclass=ABCMeta):
    def __init__(self, url: str):
        self.url = url

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    async def send_aggregated_events(self, event: AggEvent):
        pass
