from tkinter import *
import time

root = Tk()
canvas = Canvas(root, width='600', height='600')
canvas.pack()

#def bunny_draw(color):
    #ear1 = canvas.create_oval(235, 140, 275, 280, outline=color, fill=color)
    #ear2 = canvas.create_oval(335, 140, 375, 280, outline=color, fill=color)
    #body = canvas.create_oval(175, 250, 425, 550, outline=color, fill=color)
    #ground = canvas.create_rectangle(0, 500, 600, 600, outline="#5c3c2d", fill="#5c3c2d")

def bunny_draw(main, color):
    ear1 = canvas.create_oval(main/2+main/4,main/2-main/4, main, main, outline=color, fill=color)
    ear1 = canvas.create_oval(main/2+main/2,main/2-main/4, main+main/4, main, outline=color, fill=color)
    body = canvas.create_oval(main/2, main/2, main+main/2, 2*main, outline=color, fill=color)
    ground = canvas.create_rectangle(0, main+main/2, main*2, main*2, outline="#5c3c2d", fill="#5c3c2d")
bunny_draw(300, "#20d1ac")
root.mainloop()
