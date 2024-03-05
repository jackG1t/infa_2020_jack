import pygame
from pygame.draw import *


pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill([0, 128 ,128])

#draw face
circle(screen, (225,225,0), (200,200), 100)
circle(screen, (0,0,0), (200,200), 100, 3)

#draw left eye
circle(screen, (255, 0, 0), (160, 180), 25)
circle(screen, (0, 0, 0), (160, 180), 25, 2)
circle(screen, (0,0,0), (160,180), 10)

#draw right eye
circle(screen, (255, 0, 0), (240, 180), 17)
circle(screen, (0, 0, 0), (240, 180), 17, 2)
circle(screen, (0,0,0), (240,180), 10)

#draw mouth
rect(screen, (0,0,0), (160, 240, 80, 20))

#draw
line(screen, (0,0,0), (100,100),(180,150), 10)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
