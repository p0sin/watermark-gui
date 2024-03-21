from typing import Tuple
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageColor
import time

from constants import *
from menu import Menu
from widgets import *


class App(ctk.CTk):
    def  __init__(self):
        super().__init__()

        # window setup
        self.title('Watermark GUI')
        self.geometry('1000x600')
        self.minsize(800, 500)
        self.init_parameters()

        # Layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        # Canvas data
        self.image_width = 0
        self.image_height = 0
        self.canvas_width = 0
        self.canvas_height = 0

        # Create an instance of AddFile with the callback function
        self.add_file = AddFile(self, self.import_image)
        
        self.mainloop()

    def manipulate_image(self, *args):
        # Clear the canvas
        self.image_output.delete('all')

        # Reset the image to the original
        self.image = self.original.copy().convert("RGBA")

        # Create an image to draw
        txt = Image.new('RGBA', self.image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt)

        # Font 
        font_size = self.size_value.get() * 10
        text = self.watermark_text.get()
        font_family = self.font_value.get()
        
        # Check if font family is provided
        if font_family == '':
            return
        
        # Load the font
        font = ImageFont.truetype(f"{font_family.lower()}", font_size)

        # Color
        color = self.color_value.get()
        
        # Check if color is provided
        if color == '':
            return

        # Calculate opacity
        opacity = self.opacity_value.get()
        rgb_color = ImageColor.getrgb(color)
        rgb_opacity = int(opacity * 255)
        rgb = (rgb_color[0], rgb_color[1], rgb_color[2], rgb_opacity)

        # Calculate the bounding box of the text
        text_bbox = draw.textbbox((0, 0), text, font=font)

        # Calculate the position to draw the text in the center of the image
        image_width, image_height = self.image.size
        text_position = (
            (image_width - (text_bbox[2] - text_bbox[0])) // 2,
            (image_height - (text_bbox[3] - text_bbox[1])) // 2
        )

        # Draw the text at the calculated position
        draw.text(text_position, text, font=font, fill=rgb)

        # Overlay the text image onto the original image
        self.image = Image.alpha_composite(self.image, txt)

        # Place the resulting image
        self.place_image()


    def init_parameters(self):
        self.watermark_text = ctk.StringVar(value='')
        self.size_value = ctk.DoubleVar(value=10.0)
        self.font_value = ctk.StringVar(value='Arial')
        self.color_value = ctk.StringVar(value='White')
        self.opacity_value = ctk.DoubleVar(value=1.0)

        self.watermark_text.trace_add('write', self.manipulate_image)
        self.size_value.trace_add('write', self.manipulate_image)
        self.font_value.trace_add('write', self.manipulate_image)
        self.color_value.trace_add('write', self.manipulate_image)
        self.opacity_value.trace_add('write', self.manipulate_image)

    def import_image(self, path):
        self.original = Image.open(path)
        self.image = self.original
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)
        
        self.add_file.grid_forget()
        self.image_output = ImageCanvas(self, self.resize_image)
        self.menu = Menu(
            self, 
            self.size_value, 
            self.watermark_text, 
            self.font_value, 
            FONTS, 
            self.color_value, 
            COLORS,
            self.opacity_value)

    def close_edit(self):
        self.image_output.grid_forget()
        self.menu.grid_forget()

        self.add_file = AddFile(self, self.import_image)

    def resize_image(self, event): 

        # Current canvas ratio
        canvas_ratio = event.width / event.height 

        # Update canvas attributes
        self.canvas_width = event.width
        self.canvas_height = event.height

        # Resize
        if canvas_ratio > self.image_ratio: # Canvas is wider than then image
            self.image_height = int(event.height)
            self.image_width = int(self.image_height * self.image_ratio)
        else: # Canvas is taller than image
            self.image_width = int(event.width)
            self.image_height = int(self.image_width / self.image_ratio)

        self.place_image()

    def place_image(self):
        self.image_output.delete('all')
        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(self.canvas_width / 2, self.canvas_height / 2, image=self.image_tk)
    
    

App()