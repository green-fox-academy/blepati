from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def stair(size, many):
    x = 0
    y = 0
    for i in range(many):
        canvas.create_rectangle(x, y, x + size, y + size, fill="purple")
        x += size
        y += size
        size += size

stair(10, 5)

root.mainloop()
