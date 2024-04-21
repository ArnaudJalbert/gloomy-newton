from dataclasses import dataclass

from gloomy_newton.domain.entities.entity import Entity


@dataclass(frozen=True)
class District(Entity):
    """Montreal District entity.

    Attributes:
        id: District identifier.
        name: District name.
    """

    id: int
    name: str
