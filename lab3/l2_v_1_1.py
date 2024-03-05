import pygame
from pygame.draw import *
import random

def main():
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((600, 400))
    screen.fill([128, 244, 244])

    sun_position = (530, 60) #Coordinat of sun
    
    draw_sun(screen, sun_position)

    for i in range(random.randint(1,5)):
        draw_cloud(screen, get_position_cloud(screen))
    
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

def get_position_cloud(screen):
    max_Y = screen.get_height()//4
    max_X = 2 * screen.get_height()//3

    return random.randint(0, max_X), random.randint(0, max_Y)

def draw_cloud(screen, position):
    max_fluf = 10
    min_fluf = 5
    cloud_X, cloud_Y = position
    for i in range(random.randint(min_fluf, max_fluf)):
        fluf_X = cloud_X + random.random() * max_fluf * 7
        fluf_Y = cloud_Y + random.random() * 20
        size_fluf = screen.get_height()// 10 // random.randint(1, 5)
        circle(screen, (255, 255, 255), (fluf_X, fluf_Y), size_fluf)
        circle(screen, (0, 0, 0), (fluf_X, fluf_Y), size_fluf, 1)
        
main()


















