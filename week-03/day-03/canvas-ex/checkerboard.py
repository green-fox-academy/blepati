
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
size = 40

def stair(x, y, size, many):
    for i in range(0, many):
        canvas.create_rectangle(x, y,  x + size, y + size, fill="black")
        x += size * 2

for cube in range(0, 11):
    if cube%2 == 0:
        stair(0, cube * size, size, 10)
    else:
        stair(size, cube * size, size, 10)

# fill the canvas with a checkerboard pattern.

root.mainloop()
