import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent, size, wmk_text, font, FONTS, color, COLORS, opacity):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)

        # tabs
        self.add('Add Text')
        # self.add('Add Logo')

        # widgets
        TextFrame(self.tab('Add Text'), size, wmk_text, font, FONTS, color, COLORS, opacity)
        # LogoFrame(self.tab('Add Logo'))

class TextFrame(ctk.CTkFrame):
    def __init__(self, parent, size, wmk_text, font, FONTS, color, COLORS, opacity):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        TextPanel(self, 'Text', wmk_text)
        ComboBoxPanel(self, 'Font', font, FONTS)
        ComboBoxPanel(self, 'Color', color, COLORS)
        SliderPanel(self, 'Size', size, 0.2, 40)
        SliderPanel(self, 'Opacity', opacity, 0, 1)


# class LogoFrame(ctk.CTkFrame):
#     def __init__(self, parent):
#         super().__init__(master=parent)
#         self.pack(expand=True, fill='both')