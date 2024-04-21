import unittest
from gloomy_newton.domain.entities import Street, District

STREET_NAME: str = "Ontario"
DISTRICT_ID: int = 1
DISTRICT_NAME: str = "Mercier - Hochelaga-Maisonneuve"


class TestStreet(unittest.TestCase):
    street: Street
    district: District

    def setUp(self) -> None:
        """Set up the test case."""
        self.district: District = District(id=DISTRICT_ID, name=DISTRICT_NAME)
        self.street: Street = Street(name=STREET_NAME, district=self.district)

    def test_street_creation(self) -> None:
        """Test the creation of a Street entity."""
        self.assertEqual(self.street.name, STREET_NAME)
        self.assertEqual(self.street.district, self.district)


if __name__ == "__main__":
    unittest.main()
