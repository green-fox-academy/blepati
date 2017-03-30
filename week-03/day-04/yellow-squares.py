from tkinter import *

root = Tk()
canvas = Canvas(root, width='600', height='600', bg="yellow")
canvas.pack()

def draw_square(x, y, size):
    canvas.create_rectangle(x, y, x + size, y + size, outline="black", width=1)

#def recursive_something(x, y, size):
    #draw_square(x, y, size)
    #if size > 20:
        #recursive_something(x, y, size)
        #recursive_something(x+size/3, y, size/3)
        #recursive_something(x, y+size/3, size/3)
        #recursive_something(x+size/3, y+size/3, size/3)

draw_square(20, 20, 500)
#recursive_something(10, 10, 500)

root.mainloop()
