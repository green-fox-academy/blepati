from tkinter import *

root = Tk()
canvas = Canvas(root, width='600', height='600', bg="yellow")
canvas.pack()

def draw_square(x, y, size):
    canvas.create_rectangle(x, y, x + size, y + size, outline="black", width=1)

def recursive_something(x, y, size):
    draw_square(x, y, size)
    if size > 5:
        recursive_something(x+1/3*size, y, size/3)
        recursive_something(x, y+1/3*size, size/3)
        recursive_something(x+2/3*size, y+1/3*size, size/3)
        recursive_something(x+size*1/3, y+size*2/3, size/3)

recursive_something(0, 0, 600)

root.mainloop()
