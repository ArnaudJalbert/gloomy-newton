import unittest
import pandas as pd

from gloomy_newton.infrastructure.repositories import CSVTreeRepository


class TestCSVTreeRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = CSVTreeRepository(
            "./infrastructure/repositories/csv_repository/test_data/test_data_trees.csv"
        )

    def test_get_tree_by_id(self):
        tree = self.repository.get_tree_by_id("H-10")

        self.assertEqual(tree.id, "H-10")
        self.assertEqual(tree.species.acronym, "QURU")
        self.assertEqual(tree.species.latin_name, "Quercus rubra")
        self.assertEqual(tree.species.french_name, "Chêne rouge")
        self.assertEqual(tree.species.english_name, "Red Oak")
        self.assertEqual(tree.district.id, 1)
        self.assertEqual(tree.district.name, "Ahuntsic - Cartierville")
        self.assertEqual(tree.coordinates.latitude, 45.535598)
        self.assertEqual(tree.coordinates.longitude, -73.715596)
        self.assertEqual(tree.terrain_location, "Parterre Gazonné")
        self.assertEqual(tree.in_street, False)
        self.assertEqual(tree.diameter, 34.0)
        self.assertEqual(tree.update_date, pd.Timestamp("2018-06-27T00:00:00"))


if __name__ == "__main__":
    unittest.main()
