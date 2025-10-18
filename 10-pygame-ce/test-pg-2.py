import pygame
import random

WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_RADIUS = 20
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
NUMBERS_OF_BALLS = 10

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Balls')
clock = pygame.time.Clock()


def get_random_color():
    return (random.randint(50, 200),
            random.randint(50, 200),
            random.randint(50, 200))


def create_balls(count):
    balls_list = []
    for _ in range(count):
        ball = {
            'x': random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS),
            'y': random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS),
            'speed_x': random.randint(3, 7),
            'speed_y': random.randint(3, 7),
            'color': get_random_color()
        }
        balls_list.append(ball)

    print(balls_list)
    return balls_list


balls = create_balls(NUMBERS_OF_BALLS)

def update_ball_position(balls):
    ball['x'] += ball['speed_x']
    ball['y'] += ball['speed_y']

    #
    if ball['x'] - BALL_RADIUS < 0 or ball['x'] + BALL_RADIUS > WIDTH:
        ball['speed_x'] *= -1
        ball['color'] = get_random_color()
    if ball['y'] - BALL_RADIUS < 0 or ball['y'] + BALL_RADIUS > HEIGHT:
        ball['speed_y'] *= -1
        ball['color'] = get_random_color()

def check_collision_balls(ball1, ball2):


running = True
while running:
    # 1.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # update coordinates of all balls
    for ball in balls:
        update_ball_position(balls)

    # fill screen with color
    screen.fill('skyblue')

    # draw all balls
    for ball in balls:
        pygame.draw.circle(screen, ball['color'], (ball['x'], ball['y']), BALL_RADIUS)

    # screen update
    pygame.display.flip()
    clock.tick(FPS)

# ending off all processes
pygame.quit()
