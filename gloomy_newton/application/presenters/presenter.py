from abc import ABC, abstractmethod

from gloomy_newton.application.use_cases.use_case import UseCaseOutputBoundary


class Presenter(ABC):
    @abstractmethod
    def present(self, use_case_output: UseCaseOutputBoundary):
        pass
