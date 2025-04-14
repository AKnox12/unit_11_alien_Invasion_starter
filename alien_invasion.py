import sys
import pygame
from settings import Settings
from game_status import GameStats
from Carts import Carts
from arsenal import CartArsenal
#from rocks import Rocks
from rock_fleet import RockFleet
from time import sleep

class CartBlaster:
    '''Overall class, manages game assets and behavior.'''

    def __init__(self) -> None:
        '''Initialize the game, and create game resources.'''
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_carts_count)

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
        self.game_active = True


    def run_game(self) -> None:
        '''Start of Game Loop.'''
        while self.running:
            # Notice for keyboard and mouse events.
            self._check_events()
            if self.game_active():
                self.carts.update()
                self.rock_fleet.update_fleet()
                self._check_collisions()
            # Redraw the screen during each pass through the loop.
            self._update_screen()
            self.clock.tick(self.settings.FPS)


    def _check_collisions(self) -> None:
        # check collisions for cart
        if self.carts.check_collisions(self.rock_fleet.fleet):
            self._check_game_status()

            # Subtract one life if able

        # check collisions for rocks and bottom of screen
        if self.rock_fleet.check_collisions():
            self._check_game_status()

    def _check_game_status(self) -> None:
        if self.game_stats.cart_limit > 0:
            self.game_stats.cart_limit -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False  


        # check collisions of projectiles and rocks
        collisions = self.rock_fleet.check_collisions(self.carts.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(250)

        if self.rock_fleet.check_destroyed_status():
            self._reset_level()






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
