from dataclasses import dataclass

from gloomy_newton.domain.entities.entity import Entity


@dataclass(frozen=True)
class Species(Entity):
    """Tree species entity.

    Attributes:
        acronym: Species acronym.
        latin_name: Species latin name.
        french_name: Species french name.
        english_name: Species english name.
    """

    acronym: str
    latin_name: str
    french_name: str
    english_name: str
