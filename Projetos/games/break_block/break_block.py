# pylint: disable=all
# noqa: F841
import pygame
from ui_settings import UISettings


class BrickBreaker:
    def __init__(self) -> None:
        pygame.init()
        self.ui_settings = UISettings()
        self.blocks = self.ui_settings.blocks
        while not self.ui_settings.end_game:
            self.play()
        pygame.quit()

    def player_move(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:

                if (self.ui_settings.player_settings.player.x +
                    self.ui_settings.player_settings.player_size) \
                        < self.ui_settings.screen_size[0]:

                    self.ui_settings.player_settings.player.x = \
                        self.ui_settings.player_settings.player.x + 5

            if event.key == pygame.K_LEFT:
                if self.ui_settings.player_settings.player.x > 0:
                    self.ui_settings.player_settings.player.x = \
                        self.ui_settings.player_settings.player.x - 5

    def ball_move(self):
        movement = self.ui_settings.ball_movement
        self.ui_settings.ball.x = self.ui_settings.ball.x + movement[0]
        self.ui_settings.ball.y = self.ui_settings.ball.y + movement[1]

        if self.ui_settings.ball.x <= 0:
            movement[0] = - movement[0]
        if self.ui_settings.ball.y <= 0:
            movement[1] = - movement[1]
        if self.ui_settings.ball.x + self.ui_settings.ball_size >=\
                self.ui_settings.screen_size[0]:
            movement[0] = - movement[0]
        if self.ui_settings.ball.y + self.ui_settings.ball_size >=\
                self.ui_settings.screen_size[1]:
            movement = None

        if self.ui_settings.player_settings.player.collidepoint(
                self.ui_settings.ball.x, self.ui_settings.ball.y):
            movement[1] = - movement[1]
        for block in self.blocks:
            if block.collidepoint(
                    self.ui_settings.ball.x, self.ui_settings.ball.y):
                self.blocks.remove(block)
                movement[1] = - movement[1]
        return movement

    def update_score(self, punctuation):
        font = pygame.font.Font(None, 30)
        text = font.render(f"Pontuação: {punctuation}", 1,
                           self.ui_settings.colors["punctuation"])
        self.ui_settings.screen.fill(
            self.ui_settings.colors["background"], (0, 780, 150, 30))
        self.ui_settings.screen.blit(text, (0, 780))
        if punctuation >= self.ui_settings.total_number_of_blocks:
            return True
        else:
            return False

    def play(self):
        self.ui_settings.draw_home_screen()
        self.ui_settings.draw_blocks()
        self.ui_settings.end_game = self.update_score(
            self.ui_settings.total_number_of_blocks - len(self.blocks))
        pygame.display.flip()

        for _event in pygame.event.get():
            self.event = _event
            if self.event.type == pygame.QUIT:
                self.ui_settings.end_game = True
        self.player_move(self.event)
        __ball_move = self.ball_move()

        if not __ball_move:
            self.ui_settings.end_game = True

        pygame.time.wait(5)


BrickBreaker()
