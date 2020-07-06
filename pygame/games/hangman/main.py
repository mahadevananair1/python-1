import pygame
import os
import math

# Setup display
pygame.init()
width, height = 800, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman Game!")

# Button variables
radius = 20
gap = 15
letters = []
startx = round((width - (radius * 2 + gap) * 13) / 2)
starty = 400
a = 65
for i in range(26):
    x = startx + gap * 2 +((radius * 2 + gap) * (i % 13))
    y = starty + ((i // 13) * (gap + radius * 2))
    letters.append([x, y, chr(a + i)])

# Fonts
letter_font = pygame.font.SysFont('comicsans', 40)

# Load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0

# Color
white = (255,255,255)
black = (0,0,0)

# Setup game loop
fps = 60
clock = pygame.time.Clock()
run = True

def draw():
    # White color
    win.fill(white)

    # Draw buttons
    for letter in letters:
        x, y, ltr = letter
        pygame.draw.circle(win, black, (x, y), radius, 3)
        text = letter_font.render(ltr, 1, black)
        win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150,100))
    pygame.display.update()

while run:
    clock.tick(fps)

    draw()

    # Checking the event
    for event in pygame.event.get():
        # Window close exit
        if event.type == pygame.QUIT:
            run = False
        # Track mouse postion
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr = letter
                dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                if dis <  radius:
                    print(ltr)
pygame.quit()
