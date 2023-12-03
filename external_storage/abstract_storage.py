from abc import ABCMeta, abstractmethod

from va_bas import Event


class AbstractStorage(metaclass=ABCMeta):
    def __init__(self, url: str):
        self.url = url

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    async def send_aggregated_events(self, event: Event):
        pass
