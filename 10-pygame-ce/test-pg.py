import pygame
from pygame.examples.prevent_display_stretching import BACKGROUNDCOLOR

WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_RADIUS = 20
BALL_COLOR = (255, 0, 0)
BACKGROUNDCOLOR = (0,0,0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ball')

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('skyblue')
    pygame.display.flip()

pygame.quit()