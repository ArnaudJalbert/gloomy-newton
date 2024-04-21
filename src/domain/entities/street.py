"""Street entity module."""
from dataclasses import dataclass
from .district import District


@dataclass(frozen=True)
class Street:
    """Montreal Street entity.

    Attributes:
        name: Street name.
        district: District entity.
    """
    name: str
    district: District