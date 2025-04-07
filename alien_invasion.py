import sys
import pygame

from settings import Settings

from Carts import Carts

class AlienInvasion:
    '''Overall class, manages game assets and behavior.'''

    def __init__(self) -> None:
        '''Initialize the game, and create game resources.'''
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        

        self.screen = pygame.display.set_mode((1200,800))

        pygame.display.set_caption("Alien Invasion")

        self.carts = Carts(self)
        
        # Set background color.
        self.bg_color = (230,230,230)

        self.running = True

    def run_game(self) -> None:
        '''Start of Game Loop.'''
        while self.running:
            # Notice for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.carts.blitme()

            # Most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
