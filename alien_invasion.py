import sys
import pygame
from settings import Settings
from Carts import Carts
from arsenal import CartArsenal
#from rocks import Rocks
from rock_fleet import RockFleet

class CartBlaster:
    '''Overall class, manages game assets and behavior.'''

    def __init__(self) -> None:
        '''Initialize the game, and create game resources.'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((1200,800))

        pygame.display.set_caption(self.settings.name)

        # Set background.
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_width, self.settings.screen_height))


        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)
        


        self.carts = Carts(self, CartArsenal(self))
        self.rock_fleet = RockFleet(self)
        self.rock_fleet.create_fleet()


    def run_game(self) -> None:
        '''Start of Game Loop.'''
        while self.running:
            # Notice for keyboard and mouse events.
            self._check_events()
            self.carts.update()
            self.rock_fleet.update_fleet()
            self._check_collisions()
            # Redraw the screen during each pass through the loop.
            self._update_screen()
            self.clock.tick(self.settings.FPS)


    def _check_collisions(self) -> None:
        # check collisions for cart
        if self.carts.check_collisions(self.rock_fleet.fleet):
            self._reset_level()

            # Subtract one life if able

        # check collisions for rocks and bottom of screen
        if self.rock_fleet.check_collisions():
            self._reset_level()

        # check collisions of projectiles and rocks
        collisions = self.rock_fleet.check_collisions(self.carts.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(250)





    def _reset_level(self) -> None:
        self.carts.arsenal.empty() 
        self.rock_fleet.fleet.empty()
        self.rock_fleet.create_fleet()    


    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.carts.draw()
        self.rock_fleet.draw()
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
        elif event.key == pygame.K_SPACE:
            if self.carts.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = CartBlaster()
    ai.run_game()
