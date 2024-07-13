import pygame
from game_manager import GameManager


class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((820, 800))
        pygame.display.set_caption("Brick Breaker")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_manager = GameManager()
        # self.background = pygame.image.load(
        #     "Projetos/games/break_block/images.jpeg")
        # self.background = pygame.transform.scale(self.background, (820, 800))

    def main_menu(self):
        while self.running:
            self.screen.fill(('#A7BDD9'))
            self.draw_text('Welcome to Brick Breaker', 70, ('#0D0D0D'),
                           410, 300)
            self.draw_text('Press SPACE to Play', 30,
                           ('#0D0D0D'), 400, 350)
            self.handle_events()
            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.start_game()
                    self.running = False

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
