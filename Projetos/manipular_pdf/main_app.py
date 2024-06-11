from tkinter import Tk
from configurations_app import DefaultConfigurations
from interface_app import DefaultInterface
from buttons_app import DefaultButtons
from factory_app import IAppFactory
from color_palette import ColorThemes


class DefaultAppFactory(IAppFactory):
    def __init__(self, root) -> None:
        self.root = root
        self.color = ColorThemes()
        self.configurations = self.create_settings()
        self.interface = self.create_interface()
        self.buttons = self.create_buttons()

    def create_settings(self):
        return DefaultConfigurations(self.root, self.color)

    def create_buttons(self):
        return DefaultButtons(
            self.root,
            self.interface.top_frame,
            self.interface.bottom_frame,
            self.color)

    def create_interface(self):
        return DefaultInterface(self.root,
                                self.color)


if __name__ == "__main__":
    _root = Tk()
    DefaultAppFactory(_root)
    _root.mainloop()
