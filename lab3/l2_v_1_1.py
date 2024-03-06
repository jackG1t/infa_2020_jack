import pygame
from pygame.draw import *
import random
import math

def main():
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((600, 400))
    screen.fill([128, 244, 244])

    sun_position = (530, 60) #Coordinat of sun
    
    draw_sun(screen, sun_position)
    draw_clouds(screen, random.randint(1,5))
    draw_water(screen)
    
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


def draw_water(screen):
    width = screen.get_width()
    height = screen.get_height()
    rect(screen, (0,0,224), (0, height//2 ,width, height//2))


def draw_sun(screen, position):
    circle(screen, (224, 224, 0), position, screen.get_height()//10)


def get_position_cloud(screen, N):
    max_Y = screen.get_height()//4
    max_X = round(2/3 * screen.get_height())
    half_count_cloud = math.ceil(N//2)
    
    for i in range(half_count_cloud):
        for j in range(2):
            rand_X = random.randint(i*max_X//half_count_cloud, (i+1)*max_X//half_count_cloud)
            rand_Y = random.randint(j*max_Y//2, (j+1)*max_Y//2)
            yield rand_X, rand_Y 


def draw_clouds(screen, N):
    print(f'count clouds = {N}')
    for x,y in get_position_cloud(screen, N):
        print(x,y)
        draw_cloud(screen, (x,y))


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


















