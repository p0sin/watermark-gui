import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageColor

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

        self.mouse_x = 0
        self.mouse_y = 0

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
        font_size = self.text_vars['size'].get() * 10
        text = self.text_vars['text'].get() 
        font_family = self.text_vars['font'].get() 
        
        # Check if font family is provided
        if font_family == '':
            return
        
        # Load the font
        font = ImageFont.truetype(f"{font_family.lower()}", font_size)

        # Color
        color = self.text_vars['color'].get() 
        
        # Check if color is provided
        if color == '':
            return

        # Calculate opacity
        opacity = self.text_vars['opacity'].get() 
        rgb_color = ImageColor.getrgb(color)
        rgb_opacity = int(opacity * 255)
        rgb = (rgb_color[0], rgb_color[1], rgb_color[2], rgb_opacity)

        # Calculate the position to draw the text in the center of the image
        image_width, image_height = self.image.size
        if self.mouse_y == 0 and self.mouse_x == 0:
            x_pos = image_width // 2
            y_pos = image_height // 2
        else:
            x_pos = int(self.mouse_x * image_width / self.canvas_width)
            y_pos = int(self.mouse_y * image_height / self.canvas_height)

        text_position = (x_pos, y_pos)
  
        # Draw the text at the calculated position
        draw.text(text_position, text, anchor='mm', font=font, fill=rgb)

        # Overlay the text image onto the original image
        self.image = Image.alpha_composite(self.image, txt)

        # Place the resulting image
        self.place_image()

    def get_coordinates(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

        self.manipulate_image()
     
    def init_parameters(self):
        self.text_vars = {
            'text': ctk.StringVar(value=TEXT),
            'size': ctk.DoubleVar(value=SIZE),
            'font': ctk.StringVar(value=FONT),
            'color': ctk.StringVar(value=COLOR),
            'opacity': ctk.DoubleVar(value=OPACITY)
        }

        # tracing
        for var in self.text_vars.values():
            var.trace_add('write', self.manipulate_image)

    def import_image(self, path):
        self.original = Image.open(path)
        self.image = self.original
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)
        
        self.add_file.grid_forget()
        self.image_output = ImageCanvas(self, self.resize_image, self.get_coordinates)
        self.menu = Menu(self, self.text_vars, self.close_edit, self.export_image)

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

    def export_image(self, name, path):
        export_string = f'{path}/{name}.png'
        self.image.save(export_string)
        print(export_string)
        self.close_edit()    
App()