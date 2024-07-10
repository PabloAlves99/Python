import pygame


class BallSettings:
    def __init__(self) -> None:
        self.ball_settings()

    def ball_settings(self):
        self.ball_size = 20
        self.ball = pygame.Rect(100, 700, self.ball_size, self.ball_size)
        self.ball_movement = [3, -3]
