from dataclasses import dataclass

from gloomy_newton.domain.entities.entity import Entity


@dataclass(frozen=True)
class Coordinates(Entity):
    """Coordinates entity.

    Attributes:
        latitude: Latitude.
        longitude: Longitude.
    """

    latitude: float
    longitude: float
