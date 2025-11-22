from tkinter.constants import RIGHT

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

        self.left_frames = [
            pygame.image.load(IMAGES_PATH + f"wizard_red/left_{i}.png")
            for i in range(1, 5)
        ]

        self.right_frames = [
            pygame.image.load(IMAGES_PATH + f"wizard_red/right_{i}.png")
            for i in range(1, 5)
        ]

        self.image = self.stop_image
        self.is_moving = False
        self.frame_index = 0
        self.last_frame_time = 0
        self.current_frames = self.right_frames

    def show(self):
        screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        if self.x - self.SPEED >= 0:
            self.x -= self.SPEED
        else:
            self.x = 0

        print('L', self.x)

    def move_right(self):
        if self.x + self.SPEED <= SCREEN_WIDTH - self.WIDTH:
            self.x += self.SPEED
        else:
            self.x = SCREEN_WIDTH - self.WIDTH

        print('R', self.x)

    def move(self, keys_pressed: pygame.key.ScancodeWrapper, current_time: int):

        moving_left = keys_pressed[pygame.K_LEFT]
        moving_right = keys_pressed[pygame.K_RIGHT]

        # print(moving_left, moving_right)

        self.is_moving = moving_left or moving_right

        if moving_left and not moving_right:
            self.current_frames = self.left_frames
            self.move_left()
        elif moving_right and not moving_left:
            self.current_frames = self.right_frames
            self.move_right()

        self.update_animation(current_time)

    def update_animation(self, current_time):
        if self.is_moving:
            if current_time - self.last_frame_time >= 100:
                self.frame_index = ((self.frame_index + 1) % len(self.current_frames))
                self.image = self.current_frames[self.frame_index]
                self.last_frame_time = current_time
        else:
            self.image = self.stop_image


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
        screen.blit(self.background, (0, 0))

    def play(self):
        while self.run:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            keys_pressed = pygame.key.get_pressed()
            self.player.move(keys_pressed, current_time)

            # drawing events on screen
            self._draw_background()
            self.player.show()

            pygame.display.update()
            clock.tick(FPS)
        # end while

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.play()
