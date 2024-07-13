import pygame
from random import randint


class BallSettings:
    def __init__(self) -> None:
        self.ball_settings()

    def ball_settings(self):
        self.ball_size = 20
        self.ball = pygame.Rect(randint(0, 820), 700,
                                self.ball_size, self.ball_size)
        self.ball_movement = [3, -3]
