from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def fix_rec(x, y):
    canvas.create_rectangle(x, y, (x + 50), (y + 50), fill="#20d1ac")

fix_rec(30, 40)
fix_rec(120, 89)
fix_rec(220, 200)

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

root.mainloop()
