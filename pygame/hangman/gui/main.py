import pygame
import random

pygame.init()

# Create screen
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Caption
pygame.display.set_caption("Hangman Game")

# FPS
FPS = 60
clock = pygame.time.Clock()

# Font
TITLE_FONT = pygame.font.Font("font/comic-shanns.otf", 70)

# Game variables
hangman_status = 0
words = ["IDE", "PYTHON", "DEVELOPER", "PYGAME", "VIM"]
word = random.choice(words)

# Images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# Buttons
RADIUS = 20
GAP = 10
letters = []
startx = round((WIDTH - (GAP + RADIUS * 2) * 13) / 2)
starty = 400
for i in range(26):
    x = startx + GAP * 2 + ((GAP + RADIUS * 2) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y])

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def draw():
    screen.fill((WHITE))

    # Text
    text = TITLE_FONT.render("DEVELOPER HANGMAN", True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # Hangman image
    screen.blit(images[hangman_status], (150, 100))

    # Draw buttons
    for letter in letters:
        x, y = letter
        pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 3)


run = True
while run:
    # FPS
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            print(position)

    draw()

    pygame.display.update()
