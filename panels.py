import customtkinter as ctk
from tkinter import filedialog

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

        self.data_var = data_var
        self.data_var.trace('w', self.update_text)

        ctk.CTkLabel(self, text=label).grid(row=0, column=0, sticky='w', padx=10)
        self.num_label = ctk.CTkLabel(self, text=data_var.get())
        self.num_label.grid(row=0, column=1, sticky='e', padx=10)

        ctk.CTkSlider(
            self,
            variable=self.data_var,
            from_=min_value,
            to=max_value).grid(row=1, column=0, columnspan=2)
        
    def update_text(self, *args):
        self.num_label.configure(text=f'{round(self.data_var.get(), 2)}')

class ButtonsPanel(Panel):
    def __init__(self, parent, close_func, *args):
        super().__init__(parent=parent)

        self.args = args

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1), weight=1)

        self.reset = ctk.CTkButton(self, text='Reset', command=self.reset_func)
        self.remove = ctk.CTkButton(self, text='Remove', command=close_func)

        self.pack(side='bottom')
        self.reset.grid(row=0, column=0, padx=5, pady=5)
        self.remove.grid(row=0, column=1, padx=5, pady=5)


    def reset_func(self):
        for var, value in self.args:
            var.set(value)

class FileNamePanel(Panel):
    def __init__(self, parent, name_string):
        super().__init__(parent=parent)
        
        # Data
        self.name_string = name_string
        self.name_string.trace('w', self.update_text)

        # Entry for file name
        ctk.CTkEntry(self, textvariable=self.name_string).pack(fill='x', padx=20, pady=5)

        # Preview text
        self.output = ctk.CTkLabel(self, text='')
        self.output.pack()

    def update_text(self, *args):
        if self.name_string.get():
            text = self.name_string.get().replace(' ', '_') + '.' + 'png'
            self.output.configure(text=text)

class FilePathPanel(Panel):

    def __init__(self, parent, path_string):
        super().__init__(parent=parent)

        self.path_string = path_string

        button = ctk.CTkButton(self, text='Open Explorer', command=self.get_path) 
        entry = ctk.CTkEntry(self, textvariable=self.path_string)

        button.pack(pady=10)
        entry.pack(expand=True)

    def get_path(self):
        self.path_string.set(filedialog.askdirectory())   

class SaveButton(ctk.CTkButton):
    def __init__(self, parent, export_image, name_string, path_string):
        super().__init__(master=parent, text='save', command=self.save)
        self.pack(side='bottom', pady=10)

        self.export_image = export_image
        self.name_string = name_string
        self.path_string = path_string

    def save(self):
        self.export_image(
           self.name_string.get(),
           self.path_string.get() 
        )