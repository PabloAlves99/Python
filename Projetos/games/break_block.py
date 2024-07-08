# pylint: disable=all
# noqa: F841
import pygame


class BrickBreaker:
    def __init__(self) -> None:
        pygame.init()
        self.color_settings()
        self.screen_settings()
        self.ball_settings()
        self.block_settings()
        self.game_settings()
        self.blocks = self.generate_blocks()
        while not self.end_game:
            self.play()
        pygame.quit()

    def color_settings(self):
        self.colors = {
            "ball_color": "#0D0D0D",
            "background": "#A7BDD9",
            "punctuation": "#F20707",
            "player_color": "#2651A6",
            "blocks": "#2651A6",
        }

    def screen_settings(self):
        self.screen_size = (800, 800)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Brick Breaker")

    def ball_settings(self):
        self.ball_size = 20
        self.ball = pygame.Rect(100, 500, self.ball_size, self.ball_size)
        self.player_size = 200
        self.player = pygame.Rect(0, 750, self.player_size, 15)

    def block_settings(self):
        self.num_of_blocks_in_line = 8
        self.num_of_block_rows = 10
        self.total_number_of_blocks = self.num_of_blocks_in_line * \
            self.num_of_block_rows

    def game_settings(self):
        self.end_game = False
        self.punctuation = 0
        self.ball_movement = [1, -1]

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
        pygame.draw.rect(self.screen, self.colors["player_color"], self.player)
        pygame.draw.rect(self.screen, self.colors["ball_color"], self.ball)

    def draw_blocks(self):
        for block in self.blocks:
            pygame.draw.rect(self.screen, self.colors["blocks"], block)

    def player_move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if (self.player.x + self.player_size) < self.screen_size[0]:
                    self.player.x = self.player.x + 5
            if event.key == pygame.K_LEFT:
                if self.player.x > 0:
                    self.player.x = self.player.x - 5

    def ball_move(self):
        movement = self.ball_movement
        self.ball.x = self.ball.x + movement[0]
        self.ball.y = self.ball.y + movement[1]

        if self.ball.x <= 0:
            movement[0] = - movement[0]
        if self.ball.y <= 0:
            movement[1] = - movement[1]
        if self.ball.x + self.ball_size >= self.screen_size[0]:
            movement[0] = - movement[0]
        if self.ball.y + self.ball_size >= self.screen_size[1]:
            movement = None

        if self.player.collidepoint(self.ball.x, self.ball.y):
            movement[1] = - movement[1]
        for block in self.blocks:
            if block.collidepoint(self.ball.x, self.ball.y):
                self.blocks.remove(block)
                movement[1] = - movement[1]
        return movement

    def update_score(self, punctuation):
        font = pygame.font.Font(None, 30)
        text = font.render(f"Pontuação: {punctuation}", 1,
                           self.colors["punctuation"])
        self.screen.fill(self.colors["background"], (0, 780, 150, 30))
        self.screen.blit(text, (0, 780))
        if punctuation >= self.total_number_of_blocks:
            return True
        else:
            return False

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

        pygame.time.wait(1)


BrickBreaker()
