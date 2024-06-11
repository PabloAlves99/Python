from tkinter import Tk
from factory_app import IConfigurations


class DefaultConfigurations(IConfigurations):
    def __init__(self, root: Tk, color) -> None:
        self.root = root
        self.color = color
        self.app_settings()

    def app_settings(self):
        self.root.title("Manipulador de PDF")
        self.root.minsize(580, 450)
        self.root.configure(background=self.color.bg_color)
        self.root.resizable(True, True)
