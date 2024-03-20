import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)

        # tabs
        self.add('Add Text')
        self.add('Add Logo')

        # widgets
        TextFrame(self.tab('Add Text'))
        LogoFrame(self.tab('Add Logo'))

class TextFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        TextPanel(self, 'Text')
        ComboBoxPanel(self, 'Font')
        ComboBoxPanel(self, 'Color')
        SliderPanel(self, 'Size', 0)
        SliderPanel(self, 'Opacity', 0)
        SliderPanel(self, 'Rotation', 0)


class LogoFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')