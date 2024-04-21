"""Street entity module."""
from dataclasses import dataclass
from .district import District
from .entity import Entity


@dataclass(frozen=True)
class Street(Entity):
    """Montreal Street entity.

    Attributes:
        name: Street name.
        district: District entity.
    """

    name: str
    district: District
