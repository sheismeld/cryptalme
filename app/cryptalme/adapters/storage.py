from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def list_user(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_user(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_user(self, *args, **kwargs):
        pass

    @abstractmethod
    def update_user(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_user(self, *args, **kwargs):
        pass

    @abstractmethod
    def list_alert(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_alert(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_alert(self, *args, **kwargs):
        pass

    @abstractmethod
    def update_alert(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_alert(self, *args, **kwargs):
        pass

