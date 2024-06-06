from tkinter import Frame
from factory_app import IInterface


class DefaultInterface(IInterface):
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.top_frame = Frame(self.root, bd=4, bg='#A3C9D9',
                               highlightbackground='#A9CDDA',
                               highlightthickness=3)
        self.top_frame.place(relx=0.02, rely=0.02,
                             relwidth=0.96, relheight=0.32)

        self.bottom_frame = Frame(
            self.root, bd=4, bg='#A3C9D9',
            highlightbackground='#A9CDDA',
            highlightthickness=3)
        self.bottom_frame.place(relx=0.02, rely=0.35,
                                relwidth=0.96, relheight=0.62)
