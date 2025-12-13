import sys
import pygame
import random

# --------------------------------
IMAGES_PATH: str = 'images/'
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
FPS: int = 60
# --------------------------------

# --------------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ship battle')
clock = pygame.time.Clock()


# --------------------------------
class Player:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def draw_ammo(self):
        pass


class Bullet:
    pass


class Enemy:
    def __init__(self, pos):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class Background:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class Game:
    def __init__(self):
        self.player = Player()
        self.background = Background
        self.enemies = []

        self.enemy_spawn_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_spawn_event, 500)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == self.enemy_spawn_event:
                if random.randint() < 0.7:
                    x = random.randint(25, SCREEN_WIDTH - 25)
                    y = random.randint(-50, -20)
                    self.enemies.append(Enemy((x, y)))
                pygame.time.set_timer(self.enemy_spawn_event, random.randint(300, 1200))

    def play(self):
        while True:
            dt = clock.tick(FPS) / 1000

            self.handle_events()

            pygame.display.flip()


# --------------------------------
if __name__ == "__main__":
    Game().play()
