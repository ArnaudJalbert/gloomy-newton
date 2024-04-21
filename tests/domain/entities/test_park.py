import unittest
from src.domain.entities import Park

ID: str = "0035-027"
NAME: str = "Park Lalancette"


class TestPark(unittest.TestCase):
    park: Park

    def setUp(self) -> None:
        """Set up the test case."""
        self.park: Park = Park(id=ID, name=NAME)

    def test_park_creation(self) -> None:
        """Test the creation of a Park entity."""
        self.assertEqual(self.park.id, ID)
        self.assertEqual(self.park.name, NAME)


if __name__ == "__main__":
    unittest.main()
