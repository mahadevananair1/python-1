import pygame
import os.path

# Screen
pygame.init()
black = (0, 0, 0)
line_color = (255, 255, 255)
width, height = 550, 550
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

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
current_player = "X"

first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if first.collidepoint(pos) and first_open:
                if current_player == "X":
                    screen.blit(x_img, (50, 50))
                    current_player = "O"
                else:
                    screen.blit(o_img, (50, 50))
                    current_player = "X"
                first_open = False
            if second.collidepoint(pos) and second_open:
                if current_player == "X":
                    screen.blit(x_img, (225, 50))
                    current_player = "O"
                else:
                    screen.blit(o_img, (225, 50))
                    current_player = "X"
                second_open = False
            if third.collidepoint(pos) and third_open:
                if current_player == "X":
                    screen.blit(x_img, (400, 50))
                    current_player = "O"
                else:
                    screen.blit(o_img, (400, 50))
                    current_player = "X"
                third_open = False
            if fourth.collidepoint(pos) and fourth_open:
                if current_player == "X":
                    screen.blit(x_img, (50, 225))
                    current_player = "O"
                else:
                    screen.blit(o_img, (50, 225))
                    current_player = "X"
                fourth_open = False
            if fifth.collidepoint(pos) and fifth_open:
                if current_player == "X":
                    screen.blit(x_img, (225, 225))
                    current_player = "O"
                else:
                    screen.blit(o_img, (225, 225))
                    current_player = "X"
                fifth_open = False
            if sixth.collidepoint(pos) and sixth_open:
                if current_player == "X":
                    screen.blit(x_img, (400, 225))
                    current_player = "O"
                else:
                    screen.blit(o_img, (400, 225))
                    current_player = "X"
                sixth_open = False
            if seventh.collidepoint(pos) and seventh_open:
                if current_player == "X":
                    screen.blit(x_img, (50, 400))
                    current_player = "O"
                else:
                    screen.blit(o_img, (50, 400))
                    current_player = "X"
                seventh_open = False
            if eighth.collidepoint(pos) and eighth_open:
                if current_player == "X":
                    screen.blit(x_img, (225, 400))
                    current_player = "O"
                else:
                    screen.blit(o_img, (225, 400))
                    current_player = "X"
                eighth_open = False
            if ninth.collidepoint(pos) and ninth_open:
                if current_player == "X":
                    screen.blit(x_img, (400, 400))
                    current_player = "O"
                else:
                    screen.blit(o_img, (400, 400))
                    current_player = "X"
                ninth_open = False
    pygame.display.update()
