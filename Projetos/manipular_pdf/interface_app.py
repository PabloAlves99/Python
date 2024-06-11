from tkinter import Frame
from factory_app import IInterface


class DefaultInterface(IInterface):
    def __init__(self, root, color):
        self.root = root
        self.color = color
        self.setup_ui()

    def setup_ui(self):
        self.top_frame = Frame(self.root, bd=4, bg=self.color.top_frame_color,
                               highlightbackground=self.color.border_color,
                               highlightthickness=2)
        self.top_frame.place(relx=0.02, rely=0.02,
                             relwidth=0.96, relheight=0.61)

        self.bottom_frame = Frame(
            self.root, bd=4, bg=self.color.bottom_frame_color,
            highlightbackground=self.color.border_color,
            highlightthickness=2)
        self.bottom_frame.place(relx=0.02, rely=0.63,
                                relwidth=0.96, relheight=0.35)
