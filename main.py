from typing import Tuple
import customtkinter as ctk
from PIL import Image

from widgets import *

class App(ctk.CTk):
    def  __init__(self):
        super().__init__()

        # window setup
        self.title('Watermark GUI')
        self.geometry('1000x600')
        self.minsize(1000, 600)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=6)

        # Create an instance of AddFile with the callback function
        self.add_file = AddFile(self, self.import_image)
        
        self.mainloop()

    def import_image(self, path):
        self.image = Image.open(path)
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)
        
        self.add_file.grid_forget()
        self.image_output = ImageCanvas(self, self.resize_image)
        self.edit_menu = EditMenu(self, self.close_edit)


    def close_edit(self):
        self.image_output.grid_forget()
        self.edit_menu.grid_forget()

        self.add_file = AddFile(self, self.import_image)

    def resize_image(self, event):

        # current canvas ratio
        canvas_ratio = event.width / event.height 

        # resize
        if canvas_ratio > self.image_ratio: # canvas is wider than then image
            image_height = int(event.height)
            image_width = int(image_height * self.image_ratio)
        else: # canvas is taller than image
            image_width = int(event.width)
            image_height = int(image_width / self.image_ratio)


        # place image
        self.image_output.delete('all')
        resized_image = self.image.resize((image_width, image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(event.width / 2, event.height / 2, image=self.image_tk)
        

    
    

App()