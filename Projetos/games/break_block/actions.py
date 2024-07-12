# pylint: disable=all
# noqa: F841
import pygame
from game_settings import GameSettings


class Actions(GameSettings):

    def player_move(self, event):
        self.event_handler = {
            pygame.K_RIGHT: self.move_right,
            pygame.K_LEFT: self.move_left
        }
        self.valid_key_event = event.type == pygame.KEYDOWN and \
            event.key in self.event_handler

        if self.valid_key_event:
            self.event_handler[event.key]()

    def move_right(self):
        if (self.player_settings.player.x +
            self.player_settings.player_size) \
                < self.screen_size[0]:

            self.player_settings.player.x = \
                self.player_settings.player.x + 5

    def move_left(self):
        if self.player_settings.player.x > 0:
            self.player_settings.player.x = \
                self.player_settings.player.x - 5

    def ball_move(self):
        movement = self.ball_settings.ball_movement
        self.ball_settings.ball.x += movement[0]
        self.ball_settings.ball.y += movement[1]

        movement = self.check_screen_collisions(movement)
        movement = self.check_player_collision(movement)
        movement = self.check_block_collisions(movement)

        return movement

    def check_screen_collisions(self, movement):
        if self.ball_settings.ball.x <= 0:
            movement[0] = - movement[0]

        if self.ball_settings.ball.y <= 0:
            movement[1] = - movement[1]

        if self.ball_settings.ball.x + self.ball_settings.ball_size >=\
                self.screen_size[0]:
            movement[0] = - movement[0]

        if self.ball_settings.ball.y + self.ball_settings.ball_size >=\
                self.screen_size[1]:
            self.end_game = True

        return movement

    def check_player_collision(self, movement):
        if self.player_settings.player.collidepoint(self.ball_settings.ball.x,
                                                    self.ball_settings.ball.y):
            movement[1] = -movement[1]
        return movement

    def check_block_collisions(self, movement):
        ball = self.ball_settings.ball
        for block in self.blocks:
            if block.colliderect(ball):
                self.blocks.remove(block)

                # Calcular a quantidade de sobreposição em cada direção
                overlap_left = ball.right - block.left
                overlap_right = block.right - ball.left
                overlap_top = ball.bottom - block.top
                overlap_bottom = block.bottom - ball.top

                # A menor sobreposição indica a direção da colisão
                if min(overlap_left, overlap_right, overlap_top, overlap_bottom) == overlap_left:
                    movement[0] = -movement[0]
                elif min(overlap_left, overlap_right, overlap_top, overlap_bottom) == overlap_right:
                    movement[0] = -movement[0]
                elif min(overlap_left, overlap_right, overlap_top, overlap_bottom) == overlap_top:
                    movement[1] = -movement[1]
                elif min(overlap_left, overlap_right, overlap_top, overlap_bottom) == overlap_bottom:
                    movement[1] = -movement[1]

        return movement
