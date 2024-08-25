import pygame as pg
from time import sleep

def figure_input(definition:int):
    run = True
    window = pg.display.set_mode((800, 800))
    points = []
    while run:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
        for pnt in points:
            ind = points.index(pnt)
            if ind+1 != len(points):
                pg.draw.line(window, (200, 200, 0), pnt, points[ind+1], 2)
        left, middle, right = pg.mouse.get_pressed()
        if left:
            sleep(0.5)
            pos = pg.mouse.get_pos()
            points.append(pos)
            pg.draw.circle(window, (200, 200, 0), pos, 5)
        elif middle or right:
            if len(points) >= 2:
                origin = points[0]
                for pnt in points:
                    points[points.index(pnt)] = ((pnt[0]/origin[0])*definition, (pnt[1]/origin[1])*definition)
                pg.quit()
                return points
        pg.display.update()

if __name__ == "__main__":
    print(figure_input())
