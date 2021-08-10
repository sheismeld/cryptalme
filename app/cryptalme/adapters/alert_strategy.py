from abc import ABC, abstractmethod


class AlertStrategy(ABC):
    @abstractmethod
    def execute(self):
        pass
