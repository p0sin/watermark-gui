import customtkinter as ctk
from panels import *
from constants import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent, text_vars, close_func, export_image):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)

        # tabs
        self.add('Add Text')
        self.add('Export')

        # widgets
        TextFrame(self.tab('Add Text'), text_vars, close_func)
        ExportFrame(self.tab('Export'), export_image)

class TextFrame(ctk.CTkFrame):
    def __init__(self, parent, text_vars, close_func):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        TextPanel(self, 'Text', text_vars['text'])
        ComboBoxPanel(self, 'Font', text_vars['font'], FONTS)
        ComboBoxPanel(self, 'Color', text_vars['color'], COLORS)
        SliderPanel(self, 'Size', text_vars['size'], 0.2, 40)
        SliderPanel(self, 'Opacity', text_vars['opacity'], 0, 1)
        ButtonsPanel(self, 
                close_func, 
                (text_vars['text'], TEXT), 
                (text_vars['font'], FONT),
                (text_vars['color'], COLOR),
                (text_vars['size'], SIZE),
                (text_vars['opacity'], OPACITY))

class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent, export_image):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        # Data
        self.name_string = ctk.StringVar()
        self.path_string = ctk.StringVar()

        # Widgets
        FileNamePanel(self, self.name_string)
        FilePathPanel(self, self.path_string)
        SaveButton(self, export_image, self.name_string, self.path_string)