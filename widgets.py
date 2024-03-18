import customtkinter as ctk
from PIL import Image, ImageTk
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
        
    
class EditMenu(ctk.CTkFrame):
    def __init__(self, parent, close_edit):
        super().__init__(parent)

        # labels
        self.label1 = ctk.CTkLabel(self, text='Text')
        self.label2 = ctk.CTkLabel(self, text='Font')
        self.label3 = ctk.CTkLabel(self, text='Color')
        self.label4 = ctk.CTkLabel(self, text='Size')
        self.label5 = ctk.CTkLabel(self, text='Opacity')
        self.label6 = ctk.CTkLabel(self, text='Rotation')

        # widgets
        self.title = ctk.CTkLabel(self, text='Properties')
        self.text = ctk.CTkEntry(self)
        self.font = ctk.CTkComboBox(self)
        self.color = ctk.CTkComboBox(self)
        self.size = ctk.CTkSlider(self)
        self.opacity = ctk.CTkSlider(self)
        self.rotation = ctk.CTkSlider(self)
        self.close = ctk.CTkButton(self, text='Remove Photo', command=close_edit)

        # layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.rowconfigure((0,1,2,3,4,5,6,7), weight=1)


        self.grid(row=0, column=0, sticky='nsew')
        self.title.grid(row=0, column=0, columnspan=2)

        self.label1.grid(row=1, column=0)
        self.text.grid(row=1, column=1)

        self.label2.grid(row=2, column=0)
        self.font.grid(row=2, column=1)

        self.label3.grid(row=3, column=0)
        self.color.grid(row=3, column=1)

        self.label4.grid(row=4, column=0)
        self.size.grid(row=4, column=1)

        self.label5.grid(row=5, column=0)
        self.opacity.grid(row=5, column=1)

        self.label6.grid(row=6, column=0)
        self.rotation.grid(row=6, column=1)

        self.close.grid(row=7, column=0, columnspan=2)

class ImageCanvas(Canvas):
    def __init__(self, parent, resize_image):
        super().__init__(parent, bg='black', bd=0, relief='ridge', highlightthickness=0)

        # layout
        self.grid(row=0, column=1, sticky='nsew')
        self.bind('<Configure>', resize_image)

    