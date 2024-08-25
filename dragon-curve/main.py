from figure_input import figure_input
import math
if input("choose seed y/N ?  ").upper() in ["Y", "YES"]:
    points = figure_input(1)
else:
    points = [(0,0), (1,0)]
if input("non euclidian (change the value of pi) y/N ?  ").upper() in ["Y", "YES"]:
    pi = float(input("value of pi: "))
else:
    pi = math.pi
import pygame as pg

window = pg.display.set_mode((0,0), pg.FULLSCREEN)
dispinfo = pg.display.Info()
for pnt in points:
    points[points.index(pnt)] = (pnt[0] + (dispinfo.current_w/2), pnt[1] + (dispinfo.current_h/2))

def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return (qx, qy)

run = True
while run:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            run = False
    for pnt in points:
        ind = points.index(pnt)
        if ind+1 != len(points):
            pg.draw.line(window, (200, 0, 200), pnt, points[ind+1], 1)
    c = len(points)-1
    origin = points[-1]
    while c > 0:
        c -= 1
        points.append(rotate(origin, points[c], pi/2))
    pg.display.update()
