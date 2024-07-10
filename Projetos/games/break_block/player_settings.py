import pygame


class PlayerSettings:
    def __init__(self) -> None:
        self.player_settings()

    def player_settings(self):
        self.player_size = 200
        self.player = pygame.Rect(0, 750, self.player_size, 15)
