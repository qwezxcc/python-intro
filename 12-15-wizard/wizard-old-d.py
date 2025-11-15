import pygame
import random

# === Константи ===
IMAGES_PATH: str = 'images/'
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
FPS: int = 60
DIAMOND_SPEED_MIN = 2
DIAMOND_SPEED_MAX = 10
DIAMOND_SPAWN_MIN_MS = 500
DIAMOND_SPAWN_MAX_MS = 2000
DIAMOND_EVENT = pygame.USEREVENT + 1
# animation
ANIMATION_SPEED = 8

# === Ініціалізаці ===
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Чарівник')
clock = pygame.time.Clock()

# === Клас персонажу ===
class Wizard:
    pass

# === Клас діаманта ===
class Diamond:
    pass

# === Менджер діамантів ===
class Diamonds:
    pass

# === Візуальні ефекти для тексту ===
class FloatingText:
    pass

# === Основна гра ===
class Game:
    def __init__(self):
        self.run = True
        self.background = pygame.image.load(
            IMAGES_PATH + "background/background.png")
        self.player = Wizard()
        self.diamonds = Diamonds()
        self.catch = 0
        self.lost = 0
        self.effects = []
        self._setup_timer()

    def _setup_timer(self):
        pygame.time.set_timer(DIAMOND_EVENT, random.randint(DIAMOND_SPAWN_MIN_MS, DIAMOND_SPAWN_MAX_MS))


    def _draw_background(self):
        screen.blit(self.background, (0,0))


    def play(self):
        while self.run:
            # події
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()
            clock.tick(FPS)
        # end while

        pygame.quit()

# === Запуск ===
if __name__ == "__main__":
    game = Game()
    game.play()

