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
        rock_height = self.settings.rocks_height
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height


        fleet_width, fleet_height = self.calculate_fleet_size(rock_width, screen_width, rock_height, screen_height)
        x_offset, y_offset = self.calculate_offsets(rock_width, rock_height, screen_width, fleet_width, fleet_height)

        self._create_rectangle_fleet(rock_width, rock_height, fleet_width, fleet_height, x_offset, y_offset)

    def _create_rectangle_fleet(self, rock_width, rock_height, fleet_width, fleet_height, x_offset, y_offset):
        for row in range(fleet_height):
            for col in range(fleet_width):
                current_x = rock_width * col + x_offset
                current_y = rock_height * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_rock(current_x, current_y)

    def calculate_offsets(self, rock_width, rock_height, screen_width, fleet_width, fleet_height):
        half_screen = self.settings.screen_height//2
        fleet_horitzontal_space = fleet_width * rock_width
        fleet_vertival_space = fleet_height* rock_height
        x_offset = int((screen_width-fleet_horitzontal_space)//2)
        y_offset = int((half_screen-fleet_vertival_space)//2)
        return x_offset,y_offset



    def calculate_fleet_size(self, rock_width, screen_width, rock_height, screen_height):
        fleet_width = (screen_width//rock_width)
        fleet_height = ((screen_height /2)//rock_height)

        if fleet_width % 2 == 0: 
            fleet_width -= 1
        else:
            fleet_width -= 2
        
        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2

        return int(fleet_width), int(fleet_height)
    
    def _create_rock(self, current_x: int, current_y: int):
        new_rock = Rocks(self, current_x, current_y)
        
        self.fleet.add(new_rock)

    def _check_fleet_edges(self):
        rocks: Rocks
        for rocks in self.fleet:
            if rocks.check_egdes():
                self._drop_rock_fleet()
                self.fleet_direction *= -1
                break

    def _drop_rock_fleet(self) -> None:
        for rocks in self.fleet:
            rocks.y += self.fleet_drop_speed


    def update_fleet(self):
        self._check_fleet_edges()
        self.fleet.update()    

    def draw(self) -> None:
        rocks: 'Rocks'
        for rocks in self.fleet:
            rocks.draw_rocks()