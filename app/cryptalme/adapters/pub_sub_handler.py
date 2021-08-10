from abc import ABC, abstractmethod


class PubSubHandler(ABC):
    @abstractmethod
    def subscribe(self, *args, **kwargs):
        pass

    @abstractmethod
    def unsubscribe(self, *args, **kwargs):
        pass
