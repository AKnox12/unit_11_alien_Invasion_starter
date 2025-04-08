import sys
import pygame
from settings import Settings
from Carts import Carts

class CartBlaster:
    '''Overall class, manages game assets and behavior.'''

    def __init__(self) -> None:
        '''Initialize the game, and create game resources.'''
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        print(self.settings.bg_file)

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((1200,800))

        pygame.display.set_caption(self.settings.name)

        # Set background.
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_width, self.settings.screen_height))

        self.carts = Carts(self)

        self.running = True

    def run_game(self) -> None:
        '''Start of Game Loop.'''
        while self.running:
            # Notice for keyboard and mouse events.
            self._check_events()
            self.carts.update()

            # Redraw the screen during each pass through the loop.
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.carts.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.carts.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.carts.moving_left = False

    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.carts.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.carts.moving_left = True
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = CartBlaster()
    ai.run_game()
