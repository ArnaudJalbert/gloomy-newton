from datetime import datetime
from typing import Optional

import dateutil.parser
import pandas as pd

from gloomy_newton.application.repositories import TreeRepository
from gloomy_newton.domain.entities import Tree, Species, District, Street, Coordinates


class CSVTreeRepository(TreeRepository):
    _trees: pd.DataFrame = None

    def __init__(self, csv_file: str):
        self._csv_file: str = csv_file

    @property
    def trees(self):
        if self._trees is None:
            self._trees = pd.read_csv(self._csv_file, low_memory=False)
        return self._trees

    def _create_tree_from_row(self, row: pd.Series) -> Tree:
        tree_id: str = self._create_tree_id(row)
        species: Species = self._create_species(row)
        district: District = self._create_district(row)
        street: Street = self._create_street(row, district)
        coordinates: Coordinates = self._create_coordinates(row)
        terrain_location: str = self._create_terrain_location(row)
        in_street: bool = self._create_in_street(row)
        diameter: float = self._create_diameter(row)
        updated_date: datetime = self._create_updated_date(row)
        note: str = self._create_note(row)
        return Tree(
            id=tree_id,
            species=species,
            district=district,
            street=street,
            coordinates=coordinates,
            terrain_location=terrain_location,
            in_street=in_street,
            diameter=diameter,
            update_date=updated_date,
            note=note,
        )

    @staticmethod
    def _create_tree_id(row: pd.Series) -> str:
        return "-".join([str(row["INV_TYPE"].item()), str(int(row["EMP_NO"].item()))])

    @staticmethod
    def _create_species(row: pd.Series) -> Species:
        return Species(
            acronym=str(row["SIGLE"].item()),
            latin_name=str(row["Essence_latin"].item()),
            french_name=str(row["Essence_fr"].item()),
            english_name=str(row["ESSENCE_ANG"].item()),
        )

    @staticmethod
    def _create_district(row: pd.Series) -> District:
        return District(
            id=int(row["ARROND"].item()), name=str(row["ARROND_NOM"].item())
        )

    @staticmethod
    def _create_street(row: pd.Series, district: District) -> Optional[Street]:
        return (
            Street(
                name=str(row["Rue"].item()),
                district=district,
            )
            if not pd.isna(row["Rue"].item())
            else None
        )

    @staticmethod
    def _create_coordinates(row: pd.Series) -> Coordinates:
        return Coordinates(
            latitude=float(row["Latitude"].item()),
            longitude=float(row["Longitude"].item()),
        )

    @staticmethod
    def _create_terrain_location(row: pd.Series) -> Optional[str]:
        return (
            str(row["Emplacement"].item())
            if not pd.isna(row["Emplacement"].item())
            else None
        )

    @staticmethod
    def _create_in_street(row: pd.Series) -> bool:
        return row["INV_TYPE"].item() == "R"

    @staticmethod
    def _create_diameter(row: pd.Series) -> float:
        return float(row["DHP"].item())

    @staticmethod
    def _create_updated_date(row: pd.Series) -> datetime:
        return dateutil.parser.parse(str(row["Date_releve"].item()))

    @staticmethod
    def _create_note(row: pd.Series) -> Optional[str]:
        return (
            str(row["LOCALISATION"].item())
            if not pd.isna(row["LOCALISATION"].item())
            else None
        )

    def _get_row_by_tree_id(self, tree_id: str) -> pd.Series:
        tree_type, emp_number = tree_id.split("-")
        return self.trees.loc[
            (self.trees["EMP_NO"] == int(emp_number))
            & (self.trees["INV_TYPE"] == tree_type)
        ]

    def get_tree_by_id(self, tree_id: str) -> Tree:
        row = self._get_row_by_tree_id(tree_id)
        return self._create_tree_from_row(row)


if __name__ == "__main__":
    csv_tree_repository = CSVTreeRepository("./tree_data/arbres-publics.csv")
    tree = csv_tree_repository.get_tree_by_id("H-6")
    print(tree)
