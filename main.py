from typing import Tuple
import customtkinter as ctk
from PIL import Image

from widgets import *

class App(ctk.CTk):
    def  __init__(self):
        super().__init__()

        # window setup
        self.title('Watermark GUI')
        self.geometry('800x600')
        self.minsize(800, 600)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        AddFile(self)

        self.mainloop()

App()