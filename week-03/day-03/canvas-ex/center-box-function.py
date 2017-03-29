from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def center_rec(size):
    canvas.create_rectangle(150 - (size/2), 150 - (size/2), 150 + (size/2), 150 + (size/2))


center_rec(20)
center_rec(60)
center_rec(100)
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

root.mainloop()
