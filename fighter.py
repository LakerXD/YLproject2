import pygame


class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 180)
        self.vel_y = 0

    def draw_fighter(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def move(self):
        SPEED = 14
        GRAVITY = 2.5
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = +SPEED

        if key[pygame.K_SPACE] and self.rect.top + dy == 450:
            self.vel_y = -35

        self.vel_y += GRAVITY
        dy += self.vel_y


        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left
        if self.rect.right + dx > 1280:
            dx = 1280 - self.rect.right
        if self.rect.top + dy < 0:
            dy = 0 - self.rect.top
        if self.rect.top + dy > 450:
            dy = 450 - self.rect.top

        self.rect.x += dx
        self.rect.y += dy


