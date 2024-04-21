import unittest
from datetime import datetime
from gloomy_newton.domain.entities import Tree, Species, District, Street, Coordinates
from gloomy_newton.domain.value_objects import Orientation, TerrainLocation

ID: str = "R-123"
ACRONYM: str = "ABSI"
LATIN_NAME: str = "Abies balsamea"
FRENCH_NAME: str = "Sapin baumier"
ENGLISH_NAME: str = "Balsam fir"
DISTRICT_ID: int = 4
DISTRICT_NAME: str = "Mercier - Hochelaga-Maisonneuve"
STREET_NAME: str = "Ontario"
LATITUDE: float = 45.5017
LONGITUDE: float = 73.5673
TERRAIN_LOCATION: TerrainLocation = TerrainLocation.PARK
IN_STREET: bool = True
DIAMETER: float = 1.0
NOTE: str = "Test note"
ORIENTATION: Orientation = Orientation.NORTH
CIVIC_NUMBER: int = 123


class TestTree(unittest.TestCase):
    tree: Tree
    species: Species
    district: District
    street: Street
    coordinates: Coordinates

    def setUp(self) -> None:
        """Set up the test case."""
        self.species: Species = Species(
            acronym=ACRONYM,
            latin_name=LATIN_NAME,
            french_name=FRENCH_NAME,
            english_name=ENGLISH_NAME,
        )
        self.district: District = District(id=DISTRICT_ID, name=DISTRICT_NAME)
        self.street: Street = Street(name=STREET_NAME, district=self.district)
        self.coordinates: Coordinates = Coordinates(
            latitude=LATITUDE, longitude=LONGITUDE
        )

        self.tree: Tree = Tree(
            id=ID,
            species=self.species,
            district=self.district,
            street=self.street,
            coordinates=self.coordinates,
            terrain_location=TERRAIN_LOCATION.PARK.value,
            in_street=IN_STREET,
            diameter=DIAMETER,
            update_date=datetime.now(),
            note=NOTE,
            orientation=ORIENTATION,
            civic_number=CIVIC_NUMBER,
        )

    def test_tree_creation(self) -> None:
        """Test the creation of a Tree entity."""
        self.assertEqual(self.tree.id, ID)
        self.assertEqual(self.tree.species, self.species)
        self.assertEqual(self.tree.district, self.district)
        self.assertEqual(self.tree.street, self.street)
        self.assertEqual(self.tree.coordinates, self.coordinates)
        self.assertEqual(self.tree.terrain_location, TERRAIN_LOCATION.PARK.value)
        self.assertTrue(self.tree.in_street)
        self.assertEqual(self.tree.diameter, DIAMETER)
        self.assertIsInstance(self.tree.update_date, datetime)
        self.assertEqual(self.tree.note, NOTE)
        self.assertEqual(self.tree.orientation, ORIENTATION)
        self.assertEqual(self.tree.civic_number, CIVIC_NUMBER)


if __name__ == "__main__":
    unittest.main()
