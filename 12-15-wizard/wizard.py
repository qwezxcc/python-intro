import pygame
import  sys
import random

from pygame import Clock
from pygame.examples.headless_no_windows_needed import screen

# --------------------------------
IMAGES_PATH: str = 'images/'
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
FPS: int = 60
# animation
ANIMATION_SPEED = 8


# === ініціалізації ===
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Wizard')
clock = pygame.time.Clock()

# === Клас персонажу ===
class Wizard:
    pass

# === Клас діаманта ===
class Diamond:
    pass

# === Менеджер діамантів ===
class Diamond:
    pass

# === Візуальні ефекти ===
class FloatingText:
    pass

# === Основна гра ===
class Game:
    def __init__(self):
        self.run = True
    def play(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()
            clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.play()