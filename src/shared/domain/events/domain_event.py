from abc import ABC

from src.shared.domain.value_objects.domain_id import DomainId
from src.shared.utils.generate_uuid import generate_uuid


class DomainEventId(DomainId):
    pass

class DomainEvent(ABC):
    __id: DomainEventId
    def __init__(self) -> None:
        self.__id = DomainEventId(generate_uuid())
        super().__init__()

    def to_primitives(self):
        return {
            id: self.__id.value
        }
