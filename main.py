import random
import time

import pygame
from fighter import *
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Legend Stick")

clock = pygame.time.Clock()
FPS = 60

bg = pygame.image.load("assets/images/background/background.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (1280, 720))
def draw_bg():
    screen.blit(bg, (0, 0))

fighter = Fighter(280, 450)

enemy = Enemy()

run = True
while run:

    clock.tick(FPS)

    draw_bg()

    fighter.draw_fighter(screen)
    fighter.move(screen, enemy)

    enemy.draw_enemy(screen)
    enemy.enemy_move(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
