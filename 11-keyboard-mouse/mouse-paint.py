import pygame
import sys

from pygame.examples.eventlist import draw_usage_in_history

WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Keyboard testing')
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 34)

running = True

drawing = False
brush_color = BLACK
brush_size = 5
prev_pos = None
screen.fill(WHITE)

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            break
        # left
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                drawing = True

            if e.button == 2:  # start drawing
                drawing = True
                prev_pos = e.pos

            if e.button == 3:
                screen.fill(WHITE)

        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 4:
                brush_size = min(brush_size + 2, 50)
            if e.button == 5:
                brush_size = min(brush_size - 2, 1)

        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1 or e.button == 2:  # end drawing
                drawing = False
                prev_pos = None

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                brush_color = RED
            if e.key == pygame.K_g:
                brush_color = GREEN
            if e.key == pygame.K_k:
                brush_color = BLACK
            if e.key == pygame.K_b:
                brush_color = BLUE
            if e.key == pygame.K_w:
                brush_color = WHITE

    if drawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if prev_pos:
            pygame.draw.line(screen, brush_color, prev_pos, (mouse_x, mouse_y), brush_size // 2)

        pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), brush_size // 2)

    pygame.display.update()

pygame.quit()
sys.exit()
