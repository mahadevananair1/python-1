import pygame

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
player_x_change = 0

def player(x, y):
    screen.blit(player_img, (x, y))
# Game loop
running = True
while running:
    screen.fill((153, 209, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change
    player(player_x, player_y)
    pygame.display.update()