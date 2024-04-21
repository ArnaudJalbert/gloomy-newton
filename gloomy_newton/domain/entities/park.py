from dataclasses import dataclass

from gloomy_newton.domain.entities.entity import Entity


@dataclass(frozen=True)
class Park(Entity):
    """Montreal Park entity.

    Attributes:
        id: Park identifier.
        name: Park name.
    """

    id: str
    name: str
