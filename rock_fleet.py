import pygame 
from typing import TYPE_CHECKING
from rocks import Rocks

if TYPE_CHECKING:
    from alien_invasion import CartBlaster


class RockFleet:
    
    def __init__(self, game: 'CartBlaster') -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        rock_width = self.settings.rocks_width
        screen_width = self.settings.screen_width

        fleet_width = self.calculate_fleet_size(rock_width, screen_width)

#        half_screen = self.settings.screen_width
        fleet_horitzontal_space = fleet_width * rock_width
        x_offset = int((screen_width-fleet_horitzontal_space)//2)

        for col in range(fleet_width):
            current_x = rock_width * col * x_offset
            if col % 2 == 0:
                continue
            self._create_rock(current_x, 10)



    def calculate_fleet_size(self, rock_width, screen_width):
        fleet_width = (screen_width//rock_width)

        if fleet_width % 2 == 0: 
            fleet_width -= 1
        else:
            fleet_width -= 2

        return fleet_width
    
    def _create_rock(self, current_x: int, current_y: int):
        new_rock = Rocks(self, current_x, current_y)
        
        self.fleet.add(new_rock)

    def draw(self) -> None:
        rocks: 'Rocks'
        for rocks in self.fleet:
            rocks.draw_rocks()