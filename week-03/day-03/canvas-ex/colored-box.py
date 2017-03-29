from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

line = canvas.create_line(10, 10, 60, 10, fill="red")
line = canvas.create_line(60, 10, 60, 70, fill="green")
line = canvas.create_line(60, 70, 10, 70, fill="blue")
line = canvas.create_line(10, 70, 10, 10, fill="yellow")
# draw a box that has different colored lines on each edge.

root.mainloop()
