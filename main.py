from typing import Tuple
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw

from menu import Menu
from widgets import *

class App(ctk.CTk):
    def  __init__(self):
        super().__init__()

        # window setup
        self.title('Watermark GUI')
        self.geometry('1000x600')
        self.minsize(800, 500)

        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        # canvas data
        self.image_width = 0
        self.image_height = 0
        self.canvas_width = 0
        self.canvas_height = 0

        # Create an instance of AddFile with the callback function
        self.add_file = AddFile(self, self.import_image)
        
        self.mainloop()

    def manipulate_image(self, *args):
        self.image = self.original

    def import_image(self, path):
        self.original = Image.open(path)
        self.image = self.original
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)
        
        self.add_file.grid_forget()
        self.image_output = ImageCanvas(self, self.resize_image)
        self.menu = Menu(self)

    def close_edit(self):
        self.image_output.grid_forget()
        self.menu.grid_forget()

        self.add_file = AddFile(self, self.import_image)

    def resize_image(self, event): 

        # current canvas ratio
        canvas_ratio = event.width / event.height 

        # update canvas attributes
        self.canvas_width = event.width
        self.canvas_height = event.height

        # resize
        if canvas_ratio > self.image_ratio: # canvas is wider than then image
            self.image_height = int(event.height)
            self.image_width = int(self.image_height * self.image_ratio)
        else: # canvas is taller than image
            self.image_width = int(event.width)
            self.image_height = int(self.image_width / self.image_ratio)

        self.place_image()

    def place_image(self):
        self.image_output.delete('all')
        self.resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(self.resized_image)
        self.image_output.create_image(self.canvas_width / 2, self.canvas_height / 2, image=self.image_tk)
    
    

App()