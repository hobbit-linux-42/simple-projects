import pygame as pg
from random import choice
from time import sleep
import tkinter as tk
root = tk.Tk()
root.geometry("200x80")
root.title("Fractals")
root.resizable(False, False)
n = 0.0
scale = tk.Scale(root, from_=110, to=230, orient=tk.HORIZONTAL)
def quit():
    global root
    global scale
    global n
    n = scale.get()/100
    root.destroy()
btngo = tk.Button(text="GO", bg="red", comman=quit)
scale.pack()
btngo.pack()
root.mainloop()

cursor = (100, 100)
points = []
#window stuff
run = True
window = pg.display.set_mode((1000, 1000))
state = "choose"
while run:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            run = False
            
    pg.draw.circle(window, (200, 200, 0), (cursor[0], cursor[1]), 1)
    for point in points:
        pg.draw.circle(window, (0, 200, 0), (point[0], point[1]), 5)
        
    match state:
        case "draw":
            vertex = choice(points)
            cursor = (  cursor[0]-(cursor[0]-vertex[0])/n, cursor[1]-(cursor[1]-vertex[1])/n  )
        #    sleep(0.002)
        case "choose":
            left, middle, right = pg.mouse.get_pressed()
            if left:
                pos = pg.mouse.get_pos()
                points.append(pos)
                sleep(0.2)  
            elif right:
              state = "draw" 
    pg.display.update() 
