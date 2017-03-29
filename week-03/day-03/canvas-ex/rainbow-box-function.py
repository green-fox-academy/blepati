from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
rainbowcolor = ["red", "orange", "yellow", "green", "blue", "purple"]
size = 200

def center(size, color):
    for color in rainbowcolor:
        size -= 30
        canvas.create_rectangle(150 - (size/2), 150 - (size/2), 150 + (size/2), 150 + (size/2), fill=color)

center(size, rainbowcolor)
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

root.mainloop()
