from abc import ABC, abstractmethod

from gloomy_newton.domain.entities import Tree


class TreeRepository(ABC):
    @abstractmethod
    def get_tree_by_id(self, tree_id: str) -> Tree:
        pass
