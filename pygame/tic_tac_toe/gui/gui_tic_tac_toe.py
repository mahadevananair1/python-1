import pygame 
pygame.init()

white = (255, 255, 255)
line_color = (0, 0, 0)

width, height = 600, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# loading images
x_img = pygame.image.load("/home/jan/code/python/pygame/tic_tac_toe/gui/x.png")
o_img = pygame.image.load("/home/jan/code/python/pygame/tic_tac_toe/gui/o.png")

# resizing images
width_resize, height_resize = 110, 110
x_img = pygame.transform.scale(x_img, (width_resize, height_resize))
o_img = pygame.transform.scale(o_img, (width_resize, height_resize))

def draw_xo():
    global cell_one
    if cell_one is True:
        screen.blit(x_img, (100,100))


def click_to_cell():
    global cell_one
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


    # screen.blit(x_img, (25,20))
    # screen.blit(x_img, (250,20))

    draw_xo()

    pygame.display.update()
