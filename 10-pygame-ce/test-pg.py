import pygame
import random

WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_RADIUS = 20
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0,0,0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ball')
clock = pygame.time.Clock()

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 4

def get_random_color():
    return (random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255))
ball_color = get_random_color()

running = True



while running:
    # checking events in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill('skyblue')

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - BALL_RADIUS < 0 or ball_x + BALL_RADIUS > WIDTH:
        ball_speed_x *= -1
        ball_color = get_random_color()
    if ball_y - BALL_RADIUS < 0 or ball_y + BALL_RADIUS > HEIGHT:
        ball_speed_y *= -1
        ball_color = get_random_color()

    pygame.draw.circle(screen, ball_color,(ball_x, ball_y), BALL_RADIUS)


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()