from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def stair(size, many):
    x = 0
    y = 0
    for i in range(many):
        canvas.create_rectangle(x, y,  x + size, y + size, fill="purple")
        x += size
        y += size

stair(10, 12)
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

root.mainloop()
