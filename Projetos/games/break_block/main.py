import pygame
from movements import Movements


class GameManager(Movements):
    def __init__(self) -> None:
        super().__init__()
        self.initial_game()

    def initial_game(self):
        self.end_game = False
        self.punctuation = 0
        self.event = ''

    def draw_home_screen(self):
        self.screen.fill(self.colors["background"])
        pygame.draw.rect(self.screen,
                         self.colors["player_color"],
                         self.player_settings.player)

        pygame.draw.rect(self.screen,
                         self.colors["ball_color"],
                         self.ball_settings.ball)

    def draw_blocks(self):
        for block in self.blocks:
            pygame.draw.rect(self.screen,
                             self.colors["blocks"], block)

    def play(self):
        self.draw_home_screen()
        self.draw_blocks()
        self.end_game = self.update_score(
            self.total_number_of_blocks - len(self.blocks))
        pygame.display.flip()

        for _event in pygame.event.get():
            self.event = _event
            if self.event.type == pygame.QUIT:
                self.end_game = True
        self.player_move(self.event)
        __ball_move = self.ball_move()

        if not __ball_move:
            self.end_game = True

        pygame.time.wait(5)


if __name__ == "__main__":
    z = GameManager()
    pygame.init()
    while not z.end_game:
        z.play()
    pygame.quit()
