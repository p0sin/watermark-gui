import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog, Canvas

class AddFile(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # widgets
        self.label = ctk.CTkLabel(self, text='Add Watermark', font=('Arial', 20))
        self.button = ctk.CTkButton(self, text='Select File', font=('Arial', 15), command=self.open_image)

        # layout
        self.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.label.place(relx=0.5, rely=0.45, anchor='center')
        self.button.place(relx=0.5, rely=0.5, anchor='center')

    def open_image(self):
        path = filedialog.askopenfile().name
        
        return path
    
