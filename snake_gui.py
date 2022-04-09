from tkinter import *

class Grid_Data():
    def __init__(self, size, box_radius_percent, canvas_size, padding_percent):
        self.size = size
        self.spacing = (canvas_size * padding_percent) / self.size
        self.box_radii = self.spacing * box_radius_percent
        self.padding_percent = padding_percent
        self.padding_offset = (canvas_size - (canvas_size * padding_percent)) / 2


class Snake_Gui():
    def __init__(self, size, box_radius_percent, window_size, padding_percent):
        self.window = Tk()
        self.window.title("Snake, GUI Edition")
        self.window.config(bg = "grey")
        self.window.geometry(str(window_size) + "x" + str(window_size))
        self.window.resizable(False, False)

        self.canvas = Canvas(width=window_size, height=window_size, bg="white")
        self.window.update()   
        self.grid = Grid_Data(size, box_radius_percent, self.window.winfo_height(), padding_percent)
        self.canvas.pack()

    def draw_circle(self, x_pos, y_pos, radius, color="#000"):
        x1 = x_pos - (radius / 2)
        x2 = x_pos + (radius / 2)
        y1 = y_pos - (radius / 2)
        y2 = y_pos + (radius / 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="")

    def draw_rect(self, x_pos, y_pos, size, color="#EEE"):
        x1 = x_pos - (size / 2)
        x2 = x_pos + (size / 2)
        y1 = y_pos - (size / 2)
        y2 = y_pos + (size / 2)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def draw_grid(self):
        self.window.update()
        for x in range(self.grid.size):
            for y in range(self.grid.size):
                x_pos = (x * self.grid.spacing) + (self.grid.spacing * 0.5) + self.grid.padding_offset
                y_pos = (y * self.grid.spacing) + (self.grid.spacing * 0.5) + self.grid.padding_offset
                self.draw_rect(x_pos, y_pos, self.grid.box_radii)
    
