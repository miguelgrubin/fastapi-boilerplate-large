from typing import List

from abc import ABC
from dataclasses import dataclass

from src.shared.domain.events.domain_event import DomainEvent


@dataclass
class DomainModel(ABC):
    _events: List[DomainEvent] = []

    def record(self, domain_event: DomainEvent):
        self._events.append(domain_event)

    def pull_domain_events(self):
        events = self._events
        self._events = []
        return events
