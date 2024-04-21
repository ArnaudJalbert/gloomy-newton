from dataclasses import dataclass
from typing import Optional

from gloomy_newton.application.presenters import Presenter
from gloomy_newton.application.use_cases.use_case import (
    UseCase,
    UseCaseInputBoundary,
    UseCaseOutputBoundary,
)
from gloomy_newton.domain.entities import Tree


@dataclass(frozen=True)
class GetTreeByIDInputBoundary(UseCaseInputBoundary):
    tree_id: str


@dataclass(frozen=True)
class GetTreeByIDOutputBoundary(UseCaseOutputBoundary):
    tree: Optional[Tree]


class GetTreeByID(UseCase):
    def execute(
        self, use_case_input: GetTreeByIDInputBoundary, presenter: Presenter = None
    ) -> UseCaseOutputBoundary:
        tree = self._tree_repository.get_tree_by_id(use_case_input.tree_id)

        get_tree_by_id_output_boundary = GetTreeByIDOutputBoundary(tree=tree)

        if presenter:
            presenter.present(get_tree_by_id_output_boundary)

        return get_tree_by_id_output_boundary
