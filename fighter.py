import pygame


class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 180)
        self.vel_y = 0

    def draw_fighter(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def move(self, surface):
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

        if key[pygame.K_f]:
            self.attack(surface)

    def attack(self, surface):
        atacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, self.rect.x / 2.4, self.rect.height)
        pygame.draw.rect(surface, (0, 255, 0), atacking_rect)


class Enemy():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)

    def draw_enemy(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.rect)

    def enemy_move(self):
        SPEED = 10
        ddx = 0

        if self.rect.left != 0:
            ddx = -SPEED

        self.rect.x += ddx
