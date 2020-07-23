import pygame 
import os.path
pygame.init()

white = (255, 255, 255)
line_color = (0, 0, 0)

width, height = 600, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

current_player = "X"

project_directory = os.path.dirname(__file__)

# loading images
x_img = pygame.image.load(os.path.join(project_directory, "x.png"))
o_img = pygame.image.load(os.path.join(project_directory, "o.png"))
x_img = pygame.image.load("/home/jan/code/python/pygame/tic_tac_toe/gui/x.png")
o_img = pygame.image.load("/home/jan/code/python/pygame/tic_tac_toe/gui/o.png")

# resizing images
width_resize, height_resize = 110, 110
x_img = pygame.transform.scale(x_img, (width_resize, height_resize))
o_img = pygame.transform.scale(o_img, (width_resize, height_resize))

cell_one = False
cell_two = False
cell_three = False
cell_four = False
cell_five = False
cell_six = False
cell_seven = False
cell_eight = False
cell_nine = False

def draw_xo():
    global current_player
    if cell_one is True:
        screen.blit(x_img, (25,15))
        current_player = "O"
    if cell_two is True:
        screen.blit(x_img, (250, 15))
    if cell_three is True:
        screen.blit(x_img, (450, 15))
    if cell_four is True:
        screen.blit(x_img, (25, 190))
    if cell_five is True:
        screen.blit(x_img, (250, 190))
    if cell_six is True:
        screen.blit(x_img, (450, 190))
    if cell_seven is True:
        screen.blit(x_img, (25, 370))
    if cell_eight is True:
        screen.blit(x_img, (250, 370))
    if cell_nine is True:
        screen.blit(x_img, (450, 370))


def click_to_cell():
    global cell_one, cell_two, cell_three, cell_four, cell_five, cell_six, cell_seven, cell_eight, cell_nine
    if pos[0] < 200 and pos[1] < 150:
        cell_one = True
        print("Cell one")
    elif pos[0] >= 200 and pos[0] < 400 and pos[1] < 150:
        cell_two = True 
        print("Cell two")
    elif pos[0] >= 400 and pos[0] < 600 and pos[1] < 150:
        cell_three = True
        print("Cell three")
    elif pos[0] < 200 and pos[1] < 335:
        cell_four = True
        print("Cell four")
    elif pos[0] >= 200 and pos[0] < 400 and pos[1] >= 150 and pos[1] < 335:
        cell_five = True
        print("Cell five")
    elif pos[0] >= 400 and pos[0] < 595 and pos[1] >= 150 and pos[1] < 330:
        cell_six = True 
        print("Cell six")
    elif pos[0] < 200 and pos[1] < 500:
        cell_seven = True 
        print("Cell seven")
    elif pos[0] >= 200 and pos[0] < 400 and pos[1] >= 335 and pos[1] < 500:
        cell_eight = True 
        print("Cell eight")
    elif pos[0] >= 400 and pos[0] < 600 and pos[1] >= 335 and pos[1] < 500:
        cell_nine = True 
        print("Cell nine")
    
clock = pygame.time.Clock()
fps = 60

running = True 
while running:
    clock.tick(60)
    screen.fill((white))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click_to_cell()
            
    # draw vertical line on screen
    pygame.draw.line(screen, (line_color), (200, 0), (200, 500), 5)
    pygame.draw.line(screen, (line_color), (400, 0), (400, 500), 5)

    # draw horizontal line
    pygame.draw.line(screen, (line_color), (0, 150), (600, 150), 5)
    pygame.draw.line(screen, (line_color), (0, 335), (600, 335), 5)

    draw_xo()

    pygame.display.update()
