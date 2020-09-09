import os.path
import random
import pygame

# Screen for 2 players
pygame.init()
black = (0, 0, 0)
line_color = (255, 255, 255)
width, height = 550, 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Button
grey = (72, 72, 72)
bright_grey = (60, 60, 90)

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

# Fonts
font = pygame.font.Font("font/arcadeclassic.regular.ttf", 32)
over_font = pygame.font.Font('font/arcadeclassic.regular.ttf', 50)

# Global variables(Computer AI)
current_player_turn = "X"

# Human
def draw_rectangle():
    global first, second, third, fourth, fifth, sixth, seventh, eighth, ninth

    first = pygame.draw.rect(screen, line_color, (25, 25, 150, 150))
    second = pygame.draw.rect(screen, line_color, (200, 25, 150, 150))
    third = pygame.draw.rect(screen, line_color, (375, 25, 150, 150))
    fourth = pygame.draw.rect(screen, line_color, (25, 200, 150, 150))
    fifth = pygame.draw.rect(screen, line_color, (200, 200, 150, 150))
    sixth = pygame.draw.rect(screen, line_color, (375, 200, 150, 150))
    seventh = pygame.draw.rect(screen, line_color, (25, 375, 150, 150))
    eighth = pygame.draw.rect(screen, line_color, (200, 375, 150, 150))
    ninth = pygame.draw.rect(screen, line_color, (375, 375, 150, 150))

def check_win(number):
    for row in board:
        for tile in row:
            if tile == number:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == number:
                continue
            else:
                break
        else:
            return True

    for tile in range(3):
        if board[tile][tile] == number:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if board[tile][2 - tile] == number:
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
    if current_player == "X":
        x_turn_text = font.render("X turn", True, (255, 255, 255))
        screen.blit(x_turn_text, (130, 550))
        pygame.draw.rect(screen, (0, 0, 0), (120, 600, 110, 30))

def o_turn():
    if current_player == "O":
        o_turn_text = font.render("O turn", True, (255, 255, 255))
        screen.blit(o_turn_text, (130, 600))
        pygame.draw.rect(screen, (0, 0, 0), (130, 550, 110, 30))

def score_x():
    score_value = font.render("X " + str(x_score), True, (255, 255, 255))
    screen.blit(score_value, (50, 550))

def score_o():
    score_value = font.render("O " + str(o_score), True, (255, 255, 255))
    screen.blit(score_value, (50, 600))

def draw_text_won():
    global over_font

    if won_x:
        over_text = over_font.render("X won", True, (255, 0, 255))
        space_text = over_font.render("Space bar for clear", True, (255, 0, 255))
        screen.blit(over_text, (220, 200))
        screen.blit(space_text, (50, 300))

    if won_o:
        over_text = over_font.render("Computer won", True, (255, 0, 255))
        space_text = over_font.render("Space bar for clear", True, (255, 0, 255))
        screen.blit(over_text, (220, 200))
        screen.blit(space_text, (50, 300))

    """
def tie():
    global over_font

    if won_x is False or won_o is False:
        tie_text = over_font.render("Tie", True, (255, 0, 255))
        space_text = over_font.render("Space bar for clear", True, (255, 0, 255))
        screen.blit(tie_text, (220, 200))
        screen.blit(space_text, (50, 300))
        print("Game tie")
    """

# Computer(AI)
def ai():
    global current_player_turn

    while current_player_turn == "Computer":
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        print("Column", column)
        print("Row", row)

        x = [50, 225, 400][column]
        print("X", x)
        y = [50, 225, 400][row]
        print("Y", y)

        if board[row][column] == 0:
            board[row][column] = 2
            screen.blit(o_img, (x, y))
            current_player_turn = "X"

    print(board)

def flip_ai_player():
    global current_player_turn

    if current_player_turn == "X":
        current_player_turn = "Computer"
    elif current_player_turn == "Computer":
        current_player_turn = "X"

def game_intro():
    global x_score, o_score
    global won_x, won_o, won, board
    global mode_human, mode_computer, mouse, click, current_player_turn

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    mode_human = pygame.draw.rect(screen, grey, (250, 530, 160, 50))
    mode_computer = pygame.draw.rect(screen, grey, (250, 600, 160, 50))

    if mode_human.collidepoint(mouse):
        pygame.draw.rect(screen, bright_grey, (250, 530, 160, 50))
        if click[0] == 1:
            won_x = False
            won_o = False
            won = False
            x_score = 0
            o_score = 0
            board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            screen.fill((0, 0, 0))
            draw_rectangle()

    if mode_computer.collidepoint(mouse):
        pygame.draw.rect(screen, bright_grey, (250, 600, 160, 50))
        if click[0] == 1:
            won_x = False
            won_o = False
            won = False
            x_score = 0
            o_score = 0
            current_player_turn = "Computer"
            board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            screen.fill((0, 0, 0))
            draw_rectangle()

    human = font.render("2 Players", True, (255, 255, 255))
    screen.blit(human, (260, 540))

    computer = font.render("Computer", True, (255, 255, 255))
    screen.blit(computer, (260, 610))

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
                screen.fill((0, 0, 0))
                draw_rectangle()
                ai()
                flip_ai_player()

        if event.type == pygame.MOUSEBUTTONDOWN:
            global first, second, third, fourth, fifth, sixth, seventh, eighth, ninth
            global first_open, second_open, third_open, fourth_open, fifth_open
            global sixth_open, seventh_open, eighth_open, ninth_open
            global mode_human, mouse, click, mode_computer

            pos = pygame.mouse.get_pos()
            game_intro()

            if won is not True:
                global first, second, third, fourth, fifth, sixth, seventh, eighth, ninth
                global first_open, second_open, third_open, fourth_open, fifth_open
                global sixth_open, seventh_open, eighth_open, ninth_open

                if first.collidepoint(pos) and board[0][0] == 0:
                    if current_player == "X":
                        screen.blit(x_img, (50, 50))
                        board[0][0] = 1
                        ai()
                if second.collidepoint(pos) and board[0][1] == 0:
                    if current_player == "X":
                        screen.blit(x_img, (225, 50))
                        board[0][1] = 1
                        ai()
                if third.collidepoint(pos) and board[0][2] == 0:
                    if current_player == "X":
                        screen.blit(x_img, (400, 50))
                        board[0][2] = 1
                        ai()
                if fourth.collidepoint(pos) and board[1][0] == 0:
                    if current_player == "X":
                        screen.blit(x_img, (50, 225))
                        board[1][0] = 1
                        ai()
                if fifth.collidepoint(pos) and board[1][1] == 0:
                    if current_player == "X":
                        screen.blit(x_img, (225, 225))
                        board[1][1] = 1
                        ai()
                if sixth.collidepoint(pos) and board[1][2] == 0:
                    if current_player == "X":
                        screen.blit(x_img, (400, 225))
                        board[1][2] = 1
                        ai()
                if seventh.collidepoint(pos) and board[2][0] == 0:
                    if current_player == "X":
                        screen.blit(x_img, (50, 400))
                        board[2][0] = 1
                        ai()
                if eighth.collidepoint(pos) and board[2][1] == 0:
                    if current_player == "X":
                        screen.blit(x_img, (225, 400))
                        board[2][1] = 1
                        ai()
                if ninth.collidepoint(pos) and board[2][2] == 0:
                    if current_player == "X":
                        screen.blit(x_img, (400, 400))
                        board[2][2] = 1
                        ai()

                check_win(num)
                num()
                if check_win(1):
                    won = True
                    x_score += 1
                if check_win(2):
                    won = True
                    o_score += 1
                flip_ai_player()
                draw_text_won()
        game_intro()
        x_turn()
        o_turn()
        score_x()
        score_o()
    pygame.display.update()
