from tkinter import *
import time

root = Tk()
canvas = Canvas(root, width='600', height='600', bg="#ffffff")
canvas.pack()

#coord = 200, 100, 400, 300
#color = "#a6fd9c"
def icecream(x, color):
    canvas.create_arc(x, x/2, 2*x, x+x/2, start=0, extent=180, fill=color, outline=color)
    canvas.create_line(x, x, x+x/2, 2.5*x, fill="brown")
    canvas.create_line(2*x, x, x+x/2, 2.5*x, fill="brown")

icecream(100, "#a6fd9c")
root.mainloop()
