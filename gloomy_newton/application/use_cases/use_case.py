from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from gloomy_newton.application.presenters import Presenter
from gloomy_newton.application.repositories import TreeRepository


@dataclass(frozen=True)
class UseCaseInputBoundary(ABC):
    pass


@dataclass(frozen=True)
class UseCaseOutputBoundary(ABC):
    pass


class UseCase(ABC):
    def __init__(self, tree_repository: TreeRepository):
        self._tree_repository = tree_repository

    @abstractmethod
    def execute(
        self,
        use_case_input: UseCaseInputBoundary,
        presenter: Optional[Presenter] = None,
    ) -> UseCaseOutputBoundary:
        pass
