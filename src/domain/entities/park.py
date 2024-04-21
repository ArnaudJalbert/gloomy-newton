from dataclasses import dataclass


@dataclass(frozen=True)
class Park:
    """Montreal Park entity.

    Attributes:
        id: Park identifier.
        name: Park name.
    """

    id: str
    name: str
