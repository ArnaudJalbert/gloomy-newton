from dataclasses import dataclass


@dataclass(frozen=True)
class District:
    """Montreal District entity.

    Attributes:
        id: District identifier.
        name: District name.
    """

    id: int
    name: str
