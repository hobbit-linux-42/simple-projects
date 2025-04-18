from math import sqrt
from random import randint
import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
c=4
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((50, 50, 50))
    
    pygame.draw.line(screen, (200, 0, 100), (0, 0), (0, 720), 5)
    pygame.draw.line(screen, (200, 0, 100), (0, 0), (1280, 0), 5)
    pygame.draw.line(screen, (200, 0, 100), (0, 720), (1280, 720), 5)
    pygame.draw.line(screen, (200, 0, 100), (1280, 0), (1280, 720), 5)
    s=[]
    for i in range(c):
        s.append((randint(1, 1280), randint(1, 720)))
    c+=int(c/4)
    for x in range(1, 1820, 1):
        for y in range(1, 720, 1):
            l=[]
            for i in s:
                l.append(sqrt((x - i[0])**2 + (y - i[1])**2))
            p=s[l.index(min(l))]
            print((0, int((p[0]*255)/720),int((p[1]*255)/1820)))
            pygame.draw.circle(screen, (0, int((p[0]*255)/1820),int((p[1]*255)/720)), (x,y), 1)
    for i in s:
        pygame.draw.circle(screen, (200, 100, 0), i, 2)
    pygame.display.flip()
pygame.quit()
