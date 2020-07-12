import pygame
import random

pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Caption and Icon
pygame.display.set_caption('Pygame')
icon = pygame.image.load('vr-gaming.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('space-invaders.png')
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = pygame.image.load('enemy.png')
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)
enemy_x_change = 3.5
enemy_y_change = 40

# Bullet
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = 'Ready'


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'Fire'
    screen.blit(bullet_img, (x + 16, y + 10))

clock = pygame.time.Clock()


# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill((153, 209, 255))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -4
            if event.key == pygame.K_RIGHT:
                player_x_change = 4
            if event.key == pygame.K_SPACE:
                fire_bullet(player_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Checking the boundaries
    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Enemy movement
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 3.5
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -3.5
        enemy_y += enemy_y_change

    # Bullet movement

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()
