from typing import List

from dataclasses import dataclass, field

from app.shared.domain.events.domain_event import DomainEvent


@dataclass
class DomainModel:
    _events: List[DomainEvent] = field(default_factory=list)

    def record(self, domain_event: DomainEvent) -> None:
        self._events.append(domain_event)

    def pull_domain_events(self) -> List[DomainEvent]:
        events = self._events
        self._events = []
        return events
