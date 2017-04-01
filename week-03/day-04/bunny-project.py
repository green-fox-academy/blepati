from tkinter import *
import time

root = Tk()
canvas = Canvas(root, width='600', height='600')
canvas.pack()

def bunny_draw(main, color):
    ear1 = canvas.create_oval(main/2+main/4,main/2-main/4, main, main, outline=color, fill=color)
    ear1 = canvas.create_oval(main/2+main/2,main/2-main/4, main+main/4, main, outline=color, fill=color)
    body = canvas.create_oval(main/2, main/2, main+main/2, 2*main, outline=color, fill=color)

#bunny_draw(300, "#20d1ac")

def recursive_bunny(main, color):
    canvas.delete("all")
    bunny_draw(main, color)
    time.sleep(0.3)
    canvas.update()
    if main < 1000:
        return recursive_bunny(main*1.1, color)
    else:
        return 0

recursive_bunny(50, "#20d1ac")

root.mainloop()
