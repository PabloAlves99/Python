from tkinter import Frame
from factory_app import IInterface


class DefaultInterface(IInterface):
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.top_frame = Frame(self.root, bd=4, bg='#F2F2F2',
                               highlightbackground='#DDDDDC',
                               highlightthickness=2)
        self.top_frame.place(relx=0.02, rely=0.02,
                             relwidth=0.96, relheight=0.55)

        self.bottom_frame = Frame(
            self.root, bd=4, bg='#F2F2F2',
            highlightbackground='#DDDDDC',
            highlightthickness=2)
        self.bottom_frame.place(relx=0.02, rely=0.58,
                                relwidth=0.96, relheight=0.40)
