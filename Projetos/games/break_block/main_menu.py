import pygame
from game_manager import GameManager


class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Brick Breaker")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_manager = GameManager()

    def main_menu(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.draw_text('Brick Breaker', 50, (255, 255, 255), 400, 300)
            self.draw_text('Press SPACE to Play', 30,
                           (255, 255, 255), 400, 400)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start_game()
                        self.running = False

            pygame.display.flip()
            self.clock.tick(60)

    def start_game(self):
        self.game_manager.end_game = False
        while not self.game_manager.end_game:
            self.game_manager.play()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def run(self):
        self.main_menu()


if __name__ == "__main__":
    game = MainMenu()
    game.run()
