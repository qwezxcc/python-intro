import pygame
import random
import sys

# --------------------------------
IMAGES_PATH: str = 'images/'
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
FPS: int = 60
SHIP_SPEED_MIN = 2
SHIP_SPEED_MAX = 10
SHIP_SPAWN_TIME_MIN_MS = 500
SHIP_SPAWN_TIME_MAX_MS = 2000
ANIMATION_SPEED = 8
# --------------------------------

# --------------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ships')
clock = pygame.time.Clock()
# --------------------------------

# --------------------------------
class Ship_main:
    WIDTH = 150
    HEIGHT = 175
    SPEED = 10
    START_X = 10
    START_Y = 500
    TIME_FRAME: int = 100
    def __init__(self):
        self.x = self.START_X
        self.y = self.START_Y
        self.stop_image = pygame.image.load(IMAGES_PATH + 'ship_0000.png')


        self.image = self.stop_image

        def show(self):
            screen.blit(self.image, (self.x, self.y))

class Ship:
    def __init__(self, image):
        self.image = image
        self.width = self.image.get_width()
        self.y = 0
        self.x = random.randint(self.width, SCREEN_WIDTH - self.width)
        self.speed = random.randint(SHIP_SPEED_MIN, SHIP_SPEED_MAX)

        def show(self):
            x = self.x - self.image.get_width() // 2
            y = self.y
            screen.blit(self.image, (x, y))

        def fly(self):
            self.y += self.speed
class Ships:
    def __init__(self):
        self.images = self._load_images()
        self.list = []

        def _load_images(self):
            paths = ['images/ship_0001', 'images/ship_0002', 'images/ship_0003, images/ship_0004', 'images/ship_0005',
                     'images/ship_0006, images/ship_0007', 'images/ship_0008', 'images/ship_0009', 'images/ship_0010']

            return [pygame.image.load(IMAGES_PATH + p) for p in paths]

        def add(self):
            self.list.append(Ship(random.choice(self.images)))

        def draw(self):
            for ship in self.list:
                ship.show()

        def fly(self):

            for ship in self.list:
                ship.fly()

        def check_collision(self, player):
            for ship in self.list[:]:
                rect_d = ship.image.get_rect(topleft=(ship.x - ship.image.get_width() // 2, ship.y))
                rect_p = pygame.Rect(player.x, player.y, player.WIDTH, player.HEIGHT)

                if rect_p.colliderect(rect_d):
                    self.list.remove(ship)
                    return (1, ship.x, ship.y)
                elif ship.y > SCREEN_HEIGHT - 20:
                    self.list.remove(ship)
                    return (-1, ship.x, ship.y)
            return (0, None, None)
            
class Game:
    def __init__(self):
        self.run = True
        self.player = Ship()
        self.ships = Ships()
        self.catch = 0
        self.lost = 0

# --------------------------------
