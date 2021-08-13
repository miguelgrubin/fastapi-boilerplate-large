from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class VauleObject:
    def to_primitives(self):
        raise asdict(self)
