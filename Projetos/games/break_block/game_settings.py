import pygame
from player_settings import PlayerSettings
from ball_settings import BallSettings


class GameSettings():
    def __init__(self) -> None:
        self.initial_screen()
        self.initial_blocks()
        self.color_settings()
        self.player_settings = PlayerSettings()
        self.ball_settings = BallSettings()
        self.blocks = self.blocks_settings()

    def initial_screen(self):
        self.screen_size = (800, 800)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Brick Breaker")

    def initial_blocks(self):
        self.num_of_blocks_in_line = 8
        self.num_of_block_rows = 10
        self.total_number_of_blocks = self.num_of_blocks_in_line * \
            self.num_of_block_rows

    def color_settings(self):
        self.colors = {
            "ball_color": "#0D0D0D",
            "background": "#A7BDD9",
            "punctuation": "#F20707",
            "player_color": "#2651A6",
            "blocks": "#2651A6",
        }

    def blocks_settings(self):
        self.distance_between_blocks = 5
        self.block_width = self.screen_size[0] / 8 - \
            self.distance_between_blocks
        self.block_height = 15
        self.distance_between_rows = self.block_height + 10
        self._blocks = []
        return self.generate_blocks()

    def generate_blocks(self):

        for j in range(self.num_of_block_rows):

            for i in range(self.num_of_blocks_in_line):

                self.__block = pygame.Rect(
                    i * (self.block_width + self.distance_between_blocks),
                    j * self.distance_between_rows, self.block_width,
                    self.block_height)
                self._blocks.append(self.__block)

        return self._blocks

    def update_score(self, punctuation):
        font = pygame.font.Font(None, 30)
        text = font.render(f"Pontuação: {punctuation}", 1,
                           self.colors["punctuation"])
        self.screen.fill(
            self.colors["background"], (0, 780, 150, 30))
        self.screen.blit(text, (0, 780))
        if punctuation >= self.total_number_of_blocks:
            return True
        else:
            return False
