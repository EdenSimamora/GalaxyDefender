import pygame

from settings import *
from player import Player
from enemy import Enemy
from bullet import Bullet

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Defender")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = Player()

bullets = []
enemies = []

score = 0

shots_fired = 0
enemies_killed = 0

spawn_timer = 0

running = True

while running:
    clock.tick(FPS)

    spawn_timer += 1

    if spawn_timer >= 30:
        enemies.append(Enemy())
        spawn_timer = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(
                    Bullet(
                        player.rect.centerx,
                        player.rect.top
                    )
                )

        shots_fired += 1

    player.move()

    for bullet in bullets[:]:
        bullet.update()

        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    for enemy in enemies[:]:
        enemy.update()

        if enemy.rect.top > HEIGHT:
            enemies.remove(enemy)

    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):

                if bullet in bullets:
                    bullets.remove(bullet)

                if enemy in enemies:
                    enemies.remove(enemy)

                score += 1
                enemies_killed += 1
                break

    for enemy in enemies:
        if enemy.rect.colliderect(player.rect):
            running = False

    screen.fill(BLACK)

    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()

accuracy = 0

if shots_fired > 0:
    accuracy = (enemies_killed / shots_fired) * 100

print("\n===== GALAXY DEFENDER REPORT =====")
print(f"Score           : {score}")
print(f"Enemies Killed  : {enemies_killed}")
print(f"Shots Fired     : {shots_fired}")
print(f"Accuracy        : {accuracy:.1f}%")
print("==================================")

input("\nPress Enter to exit...")