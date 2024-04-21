import unittest
from gloomy_newton.domain.entities import Species

ACRONYM: str = "ABSI"
LATIN_NAME: str = "Abies balsamea"
FRENCH_NAME: str = "Sapin baumier"
ENGLISH_NAME: str = "Balsam fir"


class TestSpecies(unittest.TestCase):
    species: Species

    def setUp(self) -> None:
        """Set up the test case."""
        self.species: Species = Species(
            acronym=ACRONYM,
            latin_name=LATIN_NAME,
            french_name=FRENCH_NAME,
            english_name=ENGLISH_NAME,
        )

    def test_species_creation(self) -> None:
        """Test the creation of a Species entity."""
        self.assertEqual(self.species.acronym, ACRONYM)
        self.assertEqual(self.species.latin_name, LATIN_NAME)
        self.assertEqual(self.species.french_name, FRENCH_NAME)
        self.assertEqual(self.species.english_name, ENGLISH_NAME)


if __name__ == "__main__":
    unittest.main()
