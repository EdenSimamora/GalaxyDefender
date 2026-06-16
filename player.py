import pygame
from settings import *

class Player:
    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH // 2 - 25,
            HEIGHT - 70,
            50,
            50
        )

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        self.rect.x = max(
            0,
            min(WIDTH - self.rect.width, self.rect.x)
        )

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)