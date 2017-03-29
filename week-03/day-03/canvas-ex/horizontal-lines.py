from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def hor_lines(x, y):
    line = canvas.create_line(x, y, (x + 50), y, fill="green")

hor_lines(50, 50)
hor_lines(0, 200)
hor_lines(10, 10)

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

root.mainloop()
