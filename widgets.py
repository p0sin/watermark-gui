import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw
from tkinter import filedialog, Canvas

class AddFile(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(parent)

        self.import_func = import_func

        # widgets
        self.label = ctk.CTkLabel(self, text='Add Watermark', font=('Arial', 20))
        self.button = ctk.CTkButton(self, text='Select File', font=('Arial', 15), command=self.open_image)

        # layout
        self.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.label.place(relx=0.5, rely=0.45, anchor='center')
        self.button.place(relx=0.5, rely=0.5, anchor='center')


    def open_image(self):
        path = filedialog.askopenfile().name          
        self.import_func(path)
        

class ImageCanvas(Canvas):
    def __init__(self, parent, resize_image, get_coordinates):
        super().__init__(parent, bg='black', bd=0, relief='ridge', highlightthickness=0)

        # layout
        self.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        self.bind('<Configure>', resize_image)
        self.bind('<B1-Motion>', get_coordinates)






    