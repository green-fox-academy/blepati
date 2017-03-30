
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
paper = 300

def mid_lines(x, y):
    for i in range(0, paper, 15):
        canvas.create_line(x, y, 150, 150, fill="red")
        x += 15
    for i in range(0, paper, 15):
        canvas.create_line(x, y, 150, 150, fill="red")
        y += 15
    for i in range(0, paper, 15):
        canvas.create_line(x, y, 150, 150, fill="red")
        x -= 15
    for i in range(0, paper, 15):
        canvas.create_line(x, y, 150, 150, fill="red")
        y -= 15

mid_lines(0, 0)

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

root.mainloop()
