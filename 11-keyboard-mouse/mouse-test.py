import pygame
import sys

WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Keyboard testing')
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 34)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            break
        #left
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                print('left: ', e.pos)
        #right
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                print('right: ', e.pos)

    #стан мишки
    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (mouse_x, mouse_y), 10)

    # mouse coordinates
    text = font.render(f"X:{mouse_x}, Y:{mouse_y}", True, BLACK)
    screen.blit(text, (10, 10))


    pygame.display.update()












pygame.quit()
sys.exit()