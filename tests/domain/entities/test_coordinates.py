import unittest
from src.domain.entities import Coordinates


LATITUDE: float = 45.5017
LONGITUDE: float = 73.5673


class TestCoordinates(unittest.TestCase):
    coordinates: Coordinates

    def setUp(self) -> None:
        """Set up the test case."""
        self.coordinates: Coordinates = Coordinates(
            latitude=LATITUDE, longitude=LONGITUDE
        )

    def test_coordinates_creation(self) -> None:
        """Test the creation of a Coordinates entity."""
        self.assertEqual(self.coordinates.latitude, LATITUDE)
        self.assertEqual(self.coordinates.longitude, LONGITUDE)


if __name__ == "__main__":
    unittest.main()
