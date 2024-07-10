# pylint: disable=all
# noqa: F841
import pygame
from game_settings import GameSettings


class Movements(GameSettings):

    def player_move(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if (self.player_settings.player.x +
                    self.player_settings.player_size) \
                        < self.screen_size[0]:

                    self.player_settings.player.x = \
                        self.player_settings.player.x + 5

            if event.key == pygame.K_LEFT:
                if self.player_settings.player.x > 0:
                    self.player_settings.player.x = \
                        self.player_settings.player.x - 5

    def ball_move(self):
        movement = self.ball_settings.ball_movement
        self.ball_settings.ball.x = self.ball_settings.ball.x + movement[0]
        self.ball_settings.ball.y = self.ball_settings.ball.y + movement[1]

        if self.ball_settings.ball.x <= 0:
            movement[0] = - movement[0]
        if self.ball_settings.ball.y <= 0:
            movement[1] = - movement[1]
        if self.ball_settings.ball.x + self.ball_settings.ball_size >=\
                self.screen_size[0]:
            movement[0] = - movement[0]
        if self.ball_settings.ball.y + self.ball_settings.ball_size >=\
                self.screen_size[1]:
            movement = None

        if self.player_settings.player.collidepoint(
                self.ball_settings.ball.x, self.ball_settings.ball.y):
            movement[1] = - movement[1]

        for block in self.blocks:
            if block.collidepoint(
                    self.ball_settings.ball.x, self.ball_settings.ball.y):
                self.blocks.remove(block)
                movement[1] = - movement[1]

        return movement
