import pygame
from settings import *

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 6, 15)

    def update(self):
        self.rect.y -= BULLET_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)