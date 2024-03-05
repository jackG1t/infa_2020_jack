import pygame
from pygame.draw import *

def main():
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((600, 400))
    screen.fill([128, 244, 244])

    sun_position = (530, 60) #Coordinat of sun
    
    draw_sun(screen, sun_position)
    #draw_cloud()
    
    print(screen.get_height())
    
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()

def draw_sun(screen, position):
    circle(screen, (224, 224, 0), position, screen.get_height()//10)

def draw_cloud(screen, position):
    pass

main()
