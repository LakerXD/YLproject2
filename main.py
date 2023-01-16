import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Legend Stick")

bg = pygame.image.load("assets/images/background/background.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (1280, 720))
def draw_bg():
    screen.blit(bg, (0, 0))

run = True
while run:

    draw_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
