import pygame
from player_settings import PlayerConfigs


class UISettings():
    def __init__(self) -> None:
        self.initial_screen()
        self.initial_game()
        self.initial_blocks()
        self.color_settings()
        self.generate_blocks()
        self.ball_settings()
        self.player_settings = PlayerConfigs()
        self.blocks = self.generate_blocks()

    def initial_screen(self):
        self.screen_size = (800, 800)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Brick Breaker")

    def initial_game(self):
        self.end_game = False
        self.punctuation = 0

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

    def ball_settings(self):
        self.ball_size = 20
        self.ball = pygame.Rect(100, 700, self.ball_size, self.ball_size)
        self.ball_movement = [3, -3]

    def generate_blocks(self):
        self.distance_between_blocks = 5
        self.block_width = self.screen_size[0] / 8 - \
            self.distance_between_blocks
        self.block_height = 15
        self.distance_between_rows = self.block_height + 10
        self._blocks = []

        for j in range(self.num_of_block_rows):

            for i in range(self.num_of_blocks_in_line):

                self.__block = pygame.Rect(
                    i * (self.block_width + self.distance_between_blocks),
                    j * self.distance_between_rows, self.block_width,
                    self.block_height)
                self._blocks.append(self.__block)

        return self._blocks

    def draw_home_screen(self):
        self.screen.fill(self.colors["background"])
        pygame.draw.rect(self.screen,
                         self.colors["player_color"],
                         self.player_settings.player)

        pygame.draw.rect(self.screen,
                         self.colors["ball_color"],
                         self.ball)

    def draw_blocks(self):
        for block in self.blocks:
            pygame.draw.rect(self.screen,
                             self.colors["blocks"], block)
