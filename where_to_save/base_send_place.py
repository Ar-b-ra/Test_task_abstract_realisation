import asyncio
from abc import ABC, ABCMeta

from va_bas import Event, Metric


class BaseBroker(metaclass=ABCMeta):
    def __init__(self, url: str):
        self.url = url

    def connect(self):
        pass

    async def send_event(self, event: Event):
        pass

    async def send_metric(self, metric: Metric):
        pass
