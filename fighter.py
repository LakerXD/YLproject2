import pygame
import random


class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 180)
        self.vel_y = 0

    def draw_fighter(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def move(self, surface, target):
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
            self.attack(surface, target)

    def attack(self, surface, target):
        self.attacking = True
        atacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 1.7 * self.rect.width, self.rect.height)
        pygame.draw.rect(surface, (0, 255, 0), atacking_rect)
        if atacking_rect.colliderect(target.rect):
            print("Hit")


class Enemy():
    def __init__(self):
        self.rect = pygame.Rect(1320, random.randint(400, 600), 40, 40)


    def draw_enemy(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.rect)

    def enemy_move(self, surface):
        SPEED = 10
        ddx = 0

        if self.rect.left != -40:
            ddx = -SPEED
        else:
            self.rect = pygame.Rect(1320, random.randint(400, 600), 40, 40)

        self.rect.x += ddx
