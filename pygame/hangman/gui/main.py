import pygame
import random
import math

pygame.init()

# Create screen
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Caption
pygame.display.set_caption("Hangman Game")

# Font
TITLE_FONT = pygame.font.Font("font/comic-shanns.otf", 70)
LETTER_FONT = pygame.font.Font("font/comic-shanns.otf", 30)
WORD_FONT = pygame.font.Font("font/comic-shanns.otf", 40)

# Game variables
hangman_status = 0
words = ["IDE", "PYTHON", "DEVELOPER", "PYGAME", "VIM"]
word = random.choice(words)
guessed = ["D", "Y", "I"]
click = False

# Images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# Buttons
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)  # answer = 42
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHT_GREY = (60, 60, 90)
GREEN = (66, 244, 66)
RED = (255, 0, 0)


def draw():
    screen.fill(WHITE)

    # Text
    text = TITLE_FONT.render("DEVELOPER HANGMAN", True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # Hangman image
    screen.blit(images[hangman_status], (150, 100))

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, True, BLACK)
            # TODO(Jan): Understand the maths
            screen.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, True, BLACK)
    screen.blit(text, (400, 200))


def display_message(message):
    screen.fill(WHITE)
    text = WORD_FONT.render(message, True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    # pygame.time.delay(3000)


def menu():
    global click, hangman_status, guessed, words, word

    # FPS
    fps = 60
    clock = pygame.time.Clock()

    while True:
        # FPS
        clock.tick(fps)

        # Mouse positions
        pos_x, pos_y = pygame.mouse.get_pos()

        # Position of buttons
        pos_play_button = (50, 400, 120, 50)
        pos_quit_button = (550, 400, 120, 50)

        # Create the buttons
        button_play = pygame.Rect(pos_play_button)
        button_quit = pygame.Rect(pos_quit_button)

        # Create text inside the buttons
        text_play = WORD_FONT.render("Play", True, BLACK)
        text_quit = WORD_FONT.render("Quit", True, BLACK)

        # Check collision
        if button_play.collidepoint(pos_x, pos_y):
            pygame.draw.rect(screen, BRIGHT_GREY, pos_play_button)
            if click:
                hangman_status = 0
                words = ["IDE", "PYTHON", "DEVELOPER", "PYGAME", "VIM"]
                word = random.choice(words)
                guessed = ["D", "Y", "I"]
                click = False
                main()
        if button_quit.collidepoint(pos_x, pos_y):
            pygame.draw.rect(screen, BRIGHT_GREY, pos_quit_button)
            if click:
                pygame.quit()

        # Draw the buttons
        pygame.draw.rect(screen, GREEN, button_play)
        pygame.draw.rect(screen, RED, button_quit)

        # Draw the text
        # screen.blit(text_play, ((50 + 120) / 2, (400 + 450) / 2))
        # screen.blit(text_quit, ((550 + 120) / 2, (400 + 450) / 2))

        # screen.blit(text_play, ((50 + (120 / 2)), (400 + (50 / 2))))
        # screen.blit(text_quit, ((550 + 120) / 2, (400 + 450) / 2))

        screen.blit(text_play, (70, 405))
        screen.blit(text_quit, (570, 405))

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def main():
    global hangman_status

    # FPS
    fps = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        # FPS
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        # TODO(Jan): Understand the maths
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("You won")
            menu()
            break

        if hangman_status == 6:
            display_message("You lose")
            menu()
            break

        pygame.display.update()


main()
