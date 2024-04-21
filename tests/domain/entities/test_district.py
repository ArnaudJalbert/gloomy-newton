import unittest
from src.domain.entities import District

ID: int = 1
DISTRICT_NAME: str = "Mercier - Hochelaga-Maisonneuve"


class TestDistrict(unittest.TestCase):
    district: District

    def setUp(self) -> None:
        """Set up the test case."""
        self.district: District = District(id=ID, name=DISTRICT_NAME)

    def test_district_creation(self) -> None:
        """Test the creation of a District entity."""
        self.assertEqual(self.district.id, ID)
        self.assertEqual(self.district.name, DISTRICT_NAME)


if __name__ == "__main__":
    unittest.main()
