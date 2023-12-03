from dataclasses import dataclass
from typing import List, Union, Literal

from external_storage.abstract_storage import AbstractStorage
from va_bas import Event


@dataclass
class AggEvent:
    value: Union[int, float]
    agg_func: Literal["sum", "avg", "min", "max"]


class Aggregator:
    def __init__(self, storage: AbstractStorage):
        self.events: List[Event] = []
        self.storage = storage

    def aggregate_events(self) -> AggEvent:
        """
        Логика аггрегации событий
        :return:
        """
        pass

    def add_event(self, event: Event):
        self.events.append(event)

    def remove_event(self, event: Event):
        self.events.remove(event)
