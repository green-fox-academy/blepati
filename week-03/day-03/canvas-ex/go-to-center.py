
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def mid_lines(x, y):
    line = canvas.create_line(x, y, 150, 150, fill="red")

mid_lines(0, 0)
mid_lines(0, 50)
mid_lines(0, 100)

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

root.mainloop()
