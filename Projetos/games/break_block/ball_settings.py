import pygame
from random import randint


class BallSettings:
    def __init__(self) -> None:
        self.ball_settings()

    def ball_settings(self):
        self.ball_size = 30
        self.ball = pygame.Rect(randint(5, 820), 700,
                                self.ball_size, self.ball_size)
        self.ball_movement = [3, -3]
        self.ball_image = pygame.image.load(
            "Projetos/games/break_block/images/ball.png")
        self.ball_image = pygame.transform.scale(
            self.ball_image, (self.ball_size, self.ball_size))
