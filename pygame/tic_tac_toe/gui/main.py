import os.path
import pygame

# Screen
pygame.init()
black = (0, 0, 0)
line_color = (255, 255, 255)
width, height = 550, 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

project_directory = os.path.dirname(__file__)
# Loading images
x_img = pygame.image.load(os.path.join(project_directory, "img/x.png"))
o_img = pygame.image.load(os.path.join(project_directory, "img/o.png"))

# Resizing images
width_resize, height_resize = 110, 110
x_img = pygame.transform.scale(x_img, (width_resize, height_resize))
o_img = pygame.transform.scale(o_img, (width_resize, height_resize))

# Global variables
current_player = "X"
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
won = False
won_x = False
won_o = False
x_score = 0
o_score = 0
show_x_on_x = 50
show_y_on_x = 550
show_o_on_x = 50
show_o_on_y = 600
font = pygame.font.Font("font/arcadeclassic.regular.ttf", 32)

def draw_rectangle():
    global first, second, third, fourth, fifth, sixth, seventh, eighth, ninth
    first = pygame.draw.rect(screen, (line_color), (25, 25, 150, 150))
    second = pygame.draw.rect(screen, (line_color), (200, 25, 150, 150))
    third = pygame.draw.rect(screen, (line_color), (375, 25, 150, 150))
    fourth = pygame.draw.rect(screen, (line_color), (25, 200, 150, 150))
    fifth = pygame.draw.rect(screen, (line_color), (200, 200, 150, 150))
    sixth = pygame.draw.rect(screen, (line_color), (375, 200, 150, 150))
    seventh = pygame.draw.rect(screen, (line_color), (25, 375, 150, 150))
    eighth = pygame.draw.rect(screen, (line_color), (200, 375, 150, 150))
    ninth = pygame.draw.rect(screen, (line_color), (375, 375, 150, 150))
draw_rectangle()

def check_if_open():
    global first_open, second_open, third_open, fourth_open, fifth_open
    global sixth_open, seventh_open, eighth_open, ninth_open
    first_open = True
    second_open = True
    third_open = True
    fourth_open = True
    fifth_open = True
    sixth_open = True
    seventh_open = True
    eighth_open = True
    ninth_open = True
check_if_open()

def check_win(num):
    for row in board:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True

    for tile in range(3):
        if board[tile][tile] == num:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if board[tile][2 - tile] == num:
            continue
        else:
            break
    else:
        return True

def num():
    global won_x, won_o
    if check_win(1):
        won_x = True
    if check_win(2):
        won_o = True

def x_turn():
    if current_player == 'X':
        x_turn = font.render("X turn", True, (255, 255, 255))
        screen.blit(x_turn, (130, 550))
        pygame.draw.rect(screen, (0, 0, 0), (120, 600, 110, 30))

def o_turn():
    if current_player == 'O':
        o_turn = font.render("O turn", True, (255, 255, 255))
        screen.blit(o_turn, (130, 600))
        pygame.draw.rect(screen, (0, 0, 0), (130, 550, 110, 30))

def score_x(show_x_on_x, show_y_on_x):
    score_value = font.render("X " + str(x_score), True, (255, 255, 255))
    screen.blit(score_value, (show_x_on_x, show_y_on_x))

def score_o(show_o_on_x, show_o_on_y):
    score_value = font.render("O " + str(o_score), True, (255, 255, 255))
    screen.blit(score_value, (show_o_on_x, show_o_on_y))

def draw_text_won():
    over_font = pygame.font.Font('font/arcadeclassic.regular.ttf', 50)
    if won_x:
        over_text = over_font.render("X won", True, (255, 0, 255))
        space_text = over_font.render("Space bar for clear", True, (255, 0, 255))
        screen.blit(over_text, (220, 200))
        screen.blit(space_text, (50, 300))
    if won_o:
        over_text = over_font.render("O won", True, (255, 0, 255))
        space_text = over_font.render("Space bar for clear", True, (255, 0, 255))
        screen.blit(over_text, (220, 200))
        screen.blit(space_text, (50, 300))

clock = pygame.time.Clock()
fps = 60
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                won_x = False
                won_o = False
                won = False
                board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                check_if_open()
                screen.fill((0, 0, 0))
                draw_rectangle()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if won is not True:
                if first.collidepoint(pos) and first_open:
                    if current_player == "X":
                        screen.blit(x_img, (50, 50))
                        current_player = "O"
                        board[0][0] = 1
                    else:
                        screen.blit(o_img, (50, 50))
                        current_player = "X"
                        board[0][0] = 2
                    first_open = False
                if second.collidepoint(pos) and second_open:
                    if current_player == "X":
                        screen.blit(x_img, (225, 50))
                        current_player = "O"
                        board[0][1] = 1
                    else:
                        screen.blit(o_img, (225, 50))
                        current_player = "X"
                        board[0][1] = 2
                    second_open = False
                if third.collidepoint(pos) and third_open:
                    if current_player == "X":
                        screen.blit(x_img, (400, 50))
                        current_player = "O"
                        board[0][2] = 1
                    else:
                        screen.blit(o_img, (400, 50))
                        current_player = "X"
                        board[0][2] = 2
                    third_open = False
                if fourth.collidepoint(pos) and fourth_open:
                    if current_player == "X":
                        screen.blit(x_img, (50, 225))
                        current_player = "O"
                        board[1][0] = 1
                    else:
                        screen.blit(o_img, (50, 225))
                        current_player = "X"
                        board[1][0] = 2
                    fourth_open = False
                if fifth.collidepoint(pos) and fifth_open:
                    if current_player == "X":
                        screen.blit(x_img, (225, 225))
                        current_player = "O"
                        board[1][1] = 1
                    else:
                        screen.blit(o_img, (225, 225))
                        current_player = "X"
                        board[1][1] = 2
                    fifth_open = False
                if sixth.collidepoint(pos) and sixth_open:
                    if current_player == "X":
                        screen.blit(x_img, (400, 225))
                        current_player = "O"
                        board[1][2] = 1
                    else:
                        screen.blit(o_img, (400, 225))
                        current_player = "X"
                        board[1][2] = 2
                    sixth_open = False
                if seventh.collidepoint(pos) and seventh_open:
                    if current_player == "X":
                        screen.blit(x_img, (50, 400))
                        current_player = "O"
                        board[2][0] = 1
                    else:
                        screen.blit(o_img, (50, 400))
                        current_player = "X"
                        board[2][0] = 2
                    seventh_open = False
                if eighth.collidepoint(pos) and eighth_open:
                    if current_player == "X":
                        screen.blit(x_img, (225, 400))
                        current_player = "O"
                        board[2][1] = 1
                    else:
                        screen.blit(o_img, (225, 400))
                        current_player = "X"
                        board[2][1] = 2
                    eighth_open = False
                if ninth.collidepoint(pos) and ninth_open:
                    if current_player == "X":
                        screen.blit(x_img, (400, 400))
                        current_player = "O"
                        board[2][2] = 1
                    else:
                        screen.blit(o_img, (400, 400))
                        current_player = "X"
                        board[2][2] = 2
                    ninth_open = False

                check_win(num)
                num()
                if check_win(1):
                    won = True
                    x_score += 1
                if check_win(2):
                    won = True
                    o_score += 1
                draw_text_won()
        x_turn()
        o_turn()
        score_x(show_x_on_x, show_y_on_x)
        score_o(show_o_on_x, show_o_on_y)
    pygame.display.update()