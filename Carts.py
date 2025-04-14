import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import CartBlaster
    from arsenal import CartArsenal
class Carts:
    '''a class to manage the cart.'''
            # From the Instructor

    def __init__ (self, game: 'CartBlaster', arsenal: 'CartArsenal') -> None:
            self.game = game
            self.settings = game.settings
            self.screen = game.screen
            self.boundaries = self.screen.get_rect()

        # Load the Cart image and get rect.
            self.image = pygame.image.load('unit_11_alien_Invasion_starter/Assets/images/cart.png')
            self.image = pygame.transform.scale(self.image,
                (self.settings.cart_width, self.settings.cart_height))
            
            self.rect = self.image.get_rect()
            self._center_carts()
            # Movement for the cart
            self.moving_right = False
            self.moving_left = False

            self.arsenal = arsenal

    def _center_carts(self):
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)
    
    def update(self):
         # updating the position for the cart.
        self._Updated_ship_movement()
        self.arsenal.update_blaster()

    def _Updated_ship_movement(self):
        temp_speed = 5
        if self.moving_right and self.rect.right < self.boundaries.right:
              self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
             self.x -= temp_speed

        self.rect.x = self.x


    def draw(self) -> None:
         self.arsenal.draw()
         self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
             self._center_carts()
             return True
        return False