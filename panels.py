import customtkinter as ctk

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='#242323')
        self.pack(fill='x', pady=4, ipady=8)

class TextPanel(Panel):
    def __init__(self, parent, text):
        super().__init__(parent=parent)
        
        ctk.CTkLabel(self, text=text).pack(side='left', padx=10)
        ctk.CTkEntry(self).pack(side='left', expand=True, fill='x', padx=10)

class ComboBoxPanel(Panel):
    def __init__(self, parent, text):
        super().__init__(parent=parent)

        ctk.CTkLabel(self, text=text).pack(side='left', padx=10)
        ctk.CTkComboBox(self).pack(side='left', expand=True, fill='x', padx=10)


class SliderPanel(Panel):
    def __init__(self, parent, text, value):
        super().__init__(parent=parent)

        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1), weight=1)

        ctk.CTkLabel(self, text=text).grid(row=0, column=0, sticky='w', padx=10)
        ctk.CTkLabel(self, text=value).grid(row=0, column=1, sticky='e', padx=10)
        ctk.CTkSlider(self).grid(row=1, column=0, columnspan=2)

