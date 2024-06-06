from abc import ABC, abstractmethod


class IAppFactory(ABC):
    @abstractmethod
    def create_settings(self):
        pass

    @abstractmethod
    def create_buttons(self):
        pass

    @abstractmethod
    def create_interface(self):
        pass
