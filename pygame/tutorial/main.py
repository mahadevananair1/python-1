import pygame

# Intialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption('Pygame')
icon = pygame.image.load('vr-gaming.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('space-invaders.png')
player_x = 370
player_y = 480

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((153, 209, 255))
    pygame.display.update()