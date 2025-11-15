import pygame
import random


# --------------------------------
IMAGES_PATH: str = 'images/'
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
FPS: int = 60
DIAMOND_SPEED_MIN = 2
DIAMOND_SPEED_MAX = 10
DIAMOND_SPAWN_TIME_MIN_MS = 500
DIAMOND_SPAWN_TIME_MAX_MS = 2000
DIAMOND_EVENT = pygame.USEREVENT + 1
# animation
ANIMATION_SPEED = 8
# --------------------------------

# === ініціалізації ===
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Wizard')
clock = pygame.time.Clock()

# === Клас персонажу ===
class Wizard:
    WIDTH = 150
    HEIGHT = 175
    SPEED = 10
    START_X = 10
    START_Y = 500

    def __init__(self):
        self.x = self.START_X
        self.y = self.START_Y

        self.stop_image = pygame.image.load(IMAGES_PATH + 'wizard_red/stop_right.png')
        self.image = self.stop_image

    def show(self):
        screen.blit(self.image, (self.x, self.y))
    def move_left(self):
        pass
    def move_right(self):
        pass
    def move(self):
        pass
    def update_animation(self):
        pass



# === Клас діаманта ===
class Diamond:
    pass

# === Менеджер діамантів ===
class Diamonds:
    pass

# === Візуальні ефекти ===
class FloatingText:
    pass

# === Основна гра ===
class Game:
    def __init__(self):
        self.run = True
        self.background = pygame.image.load(IMAGES_PATH + 'background/background.png')
        self.player = Wizard()
        self.diamonds = Diamonds()
        self.catch = 0
        self.lost = 0
        self.effects = []
        self._setup_timer()

    def _setup_timer(self):
        pygame.time.set_timer(DIAMOND_EVENT, random.randint(DIAMOND_SPAWN_TIME_MIN_MS, DIAMOND_SPAWN_TIME_MAX_MS))

    def _draw_background(self):
        screen.blit(self.background, (0,0))

    def play(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False


            #
            keys = pygame.key.get_pressed()

            # drawing events on screen
            self._draw_background()
            self.player.show()


            pygame.display.update()
            clock.tick(FPS)
        #end while

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.play()
