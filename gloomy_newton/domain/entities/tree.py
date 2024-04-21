"""Module with the Tree entity."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .coordinates import Coordinates
from .district import District
from .entity import Entity
from ..value_objects import Orientation
from .park import Park
from .species import Species
from .street import Street
from ..value_objects import TerrainLocation


@dataclass
class Tree(Entity):
    """Montreal Tree entity.

    Attributes:
        id: Tree identifier.
        species: Species entity.
        district: District entity.
        street: Street entity.
        coordinates: Coordinates entity.
        terrain_location: TerrainLocation entity.
        in_street: True if the tree is in a street, False otherwise.
        diameter: Tree diameter.
        update_date: Last update date.
        note: Tree note.
        park: Park entity.
        plantation_date: Plantation date.
        orientation: Orientation entity.
        civic_number: Civic number.
    """

    id: str
    species: Species
    district: District
    coordinates: Coordinates
    terrain_location: str
    in_street: bool
    diameter: float
    update_date: datetime
    note: Optional[str]
    street: Optional[Street] = None
    park: Optional[Park] = None
    plantation_date: Optional[datetime] = None
    orientation: Optional[Orientation] = None
    civic_number: Optional[int] = None
