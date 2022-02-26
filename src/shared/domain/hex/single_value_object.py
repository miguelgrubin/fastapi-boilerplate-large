from typing import Generic, TypeVar

from dataclasses import dataclass

T = TypeVar("T")


@dataclass(frozen=True)
class SingleValueObject(Generic[T]):
    value: T

    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

    def __eq__(self, o) -> bool:
        return self.value == o.value
