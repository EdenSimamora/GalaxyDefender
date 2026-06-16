import pygame
import random
from settings import *

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(
            random.randint(0, WIDTH - 40),
            -40,
            40,
            40
        )

    def update(self):
        self.rect.y += ENEMY_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)