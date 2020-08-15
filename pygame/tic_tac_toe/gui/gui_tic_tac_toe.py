import pygame
import os.path

pygame.init()

black = (0, 0, 0)
line_color = (255, 255, 255)

width, height = 550, 550
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

current_player = "X"

project_directory = os.path.dirname(__file__)
# loading images
x_img = pygame.image.load(os.path.join(project_directory, "x.png"))
o_img = pygame.image.load(os.path.join(project_directory, "o.png"))

# resizing images
width_resize, height_resize = 110, 110
x_img = pygame.transform.scale(x_img, (width_resize, height_resize))
o_img = pygame.transform.scale(o_img, (width_resize, height_resize))

# Draw rectangle
first = pygame.draw.rect(screen, (line_color), (25, 25, 150, 150))
second = pygame.draw.rect(screen, (line_color), (200, 25, 150, 150))
third = pygame.draw.rect(screen, (line_color), (375, 25, 150, 150))

fourth = pygame.draw.rect(screen, (line_color), (25, 200, 150, 150))
fifth = pygame.draw.rect(screen, (line_color), (200, 200, 150, 150))
sixth = pygame.draw.rect(screen, (line_color), (375, 200, 150, 150))

seventh = pygame.draw.rect(screen, (line_color), (25, 375, 150, 150))
eighth = pygame.draw.rect(screen, (line_color), (200, 375, 150, 150))
ninth = pygame.draw.rect(screen, (line_color), (375, 375, 150, 150))

clock = pygame.time.Clock()
fps = 60

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

            if first.collidepoint(pos):
                screen.blit(x_img, (50, 50))
            if second.collidepoint(pos):
                screen.blit(x_img, (225, 50))
            if third.collidepoint(pos):
                screen.blit(x_img, (400, 50))
            if fourth.collidepoint(pos):
                pygame.draw.rect(screen, (255, 0, 0), (50, 225, 100, 100))
            if fifth.collidepoint(pos):
                pygame.draw.rect(screen, (255, 0, 0), (225, 225, 100, 100))
            if sixth.collidepoint(pos):
                pygame.draw.rect(screen, (255, 0, 0), (400, 225, 100, 100))

            if seventh.collidepoint(pos):
                pygame.draw.rect(screen, (255, 0, 0), (50, 400, 100, 100))
            if eighth.collidepoint(pos):
                pygame.draw.rect(screen, (255, 0, 0), (225, 400, 100, 100))
            if ninth.collidepoint(pos):
                pygame.draw.rect(screen, (255, 0, 0), (400, 400, 100, 100))
    pygame.display.update()
