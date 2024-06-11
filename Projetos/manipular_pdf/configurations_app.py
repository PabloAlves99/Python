from tkinter import Tk
from factory_app import IConfigurations


class DefaultConfigurations(IConfigurations):
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.app_settings()

    def app_settings(self):
        self.root.title("Manipulador de PDF")
        self.root.minsize(430, 350)
        self.root.configure(background='#A3C9D9')
        self.root.resizable(True, True)
