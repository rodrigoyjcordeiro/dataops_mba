from abc import ABC, abstractmethod


class Step(ABC):

    @abstractmethod
    def exec(self, **kwargs):
        pass
