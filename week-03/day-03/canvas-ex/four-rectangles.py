from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def four_rec(x, y, z, color):
    canvas.create_rectangle(x, y, (x + z), (y + z), fill=color)

four_rec(27, 34, 10, "red")
four_rec(10, 134, 100, "blue")
four_rec(100, 100, 30, "#ededed")
four_rec(150, 120, 70, "yellow")
# draw four different size and color rectangles.

root.mainloop()
