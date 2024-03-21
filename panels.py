import customtkinter as ctk

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='#242323')
        self.pack(fill='x', pady=4, ipady=8)

class TextPanel(Panel):
    def __init__(self, parent, label, wmk_text):
        super().__init__(parent=parent)
        
        ctk.CTkLabel(self, text=label).pack(side='left', padx=10)
        self.wmk_text = ctk.CTkEntry(self, textvariable=wmk_text)
        self.wmk_text.pack(side='left', expand=True, fill='x', padx=10)

class ComboBoxPanel(Panel):
    def __init__(self, parent, label, value, list):
        super().__init__(parent=parent)

        ctk.CTkLabel(self, text=label).pack(side='left', padx=10)
        ctk.CTkComboBox(
            self,
            values=list,
            variable=value).pack(side='left', expand=True, fill='x', padx=10)


class SliderPanel(Panel):
    def __init__(self, parent, label, data_var, min_value, max_value):
        super().__init__(parent=parent)

        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1), weight=1)

        ctk.CTkLabel(self, text=label).grid(row=0, column=0, sticky='w', padx=10)
        self.num_label = ctk.CTkLabel(self, text=data_var.get())
        self.num_label.grid(row=0, column=1, sticky='e', padx=10)

        ctk.CTkSlider(
            self,
            variable=data_var,
            from_=min_value,
            to=max_value,
            command=self.update_text).grid(row=1, column=0, columnspan=2)
        
    def update_text(self, value):
        self.num_label.configure(text=f'{round(value, 2)}')

