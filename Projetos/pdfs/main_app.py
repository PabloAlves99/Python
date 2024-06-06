from tkinter import Tk
from configurations_app import DefaultConfigurations
from interface_app import DefaultInterface
from buttons_app import DefaultButtons
from factory_app import IAppFactory


class DefaultAppFactory(IAppFactory):
    def __init__(self, root) -> None:
        self.root = root
        self.configurations = self.create_settings()
        self.interface = self.create_interface()
        self.buttons = self.create_buttons()

    def create_settings(self):
        return DefaultConfigurations(self.root)

    def create_buttons(self):
        return DefaultButtons(self.root, self.interface.top_frame)

    def create_interface(self):
        return DefaultInterface(self.root)


if __name__ == "__main__":
    _root = Tk()
    DefaultAppFactory(_root)
    _root.mainloop()
