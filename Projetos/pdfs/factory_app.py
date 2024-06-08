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


class IConfigurations(ABC):
    @abstractmethod
    def app_settings(self):
        pass


class IButtons(ABC):
    @abstractmethod
    def show_buttons(self):
        pass

    @abstractmethod
    def create_buttons(self):
        pass


class IInterface(ABC):
    @abstractmethod
    def setup_ui(self):
        pass
