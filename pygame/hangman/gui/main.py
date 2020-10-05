import pygame

pygame.init()

# Create screen
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Caption
pygame.display.set_caption("Hangman")

# FPS
clock = pygame.time.Clock()

# Font
TITLE_FONT = pygame.font.Font("font/comic-shanns.otf", 70)

# Colors
BLACK = (0, 0, 0)

# Game variables
hangman_status = 0

# Images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)
    screen.blit(images[hangman_status], (150, 100))


def draw():
    screen.fill((255, 255, 255))

    # Text
    text = TITLE_FONT.render("DEVELOPER HANGMAN", True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))


run = True
while run:
    # FPS
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw()

    pygame.display.update()
