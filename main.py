from asyncio.windows_events import NULL
import random
from time import sleep
from tkinter import Canvas
import snake_gui

def main():
    gui = snake_gui.Snake_Gui(15, 0.9, 800, 0.95)
    gameloop(gui)
    gui.window.mainloop()


def gameloop(gui):
    # Cleanup
    gui.canvas.delete("all")
    
    # Draw
    gui.draw_grid()
    gui.draw_circle(100, 100, 100, generateColor())
    gui.canvas.pack()

    # Prep next call
    gui.window.after(1000, gameloop, gui)
        

def generateColor():
    arr = "#"
    for i in range(6):
       arr += str(random.randint(0, 9))
    return arr

if __name__ == '__main__':
    main()