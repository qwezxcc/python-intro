import pygame
import sys

WIDTH, HEIGHT = 600, 400
pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Keyboard testing')
clock = pygame.time.Clock()

running = True
while running:
    #event of keyboard in "event"
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            print('all events: ', e.key)
        if e.type == pygame.QUIT:
            running = False
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
      print('right')
    if keys[pygame.K_LEFT]:
      print('left')

    pygame.display.update()
    clock.tick(60)
















pygame.quit()
sys.exit()