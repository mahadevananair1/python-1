import pygame 
pygame.init()

width, height = 700, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (255,0,0), (100,100), (300,200), 5)

    pygame.display.update()