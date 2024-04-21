from dataclasses import dataclass


@dataclass(frozen=True)
class Species:
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
