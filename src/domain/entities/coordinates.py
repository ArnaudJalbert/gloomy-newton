from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates:
    """Coordinates entity.

    Attributes:
        latitude: Latitude.
        longitude: Longitude.
    """

    latitude: float
    longitude: float
