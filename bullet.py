import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import CartBlaster

class Bullet(Sprite):
    def __init__(self, game: 'CartBlaster') -> None: 
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.bullet_width, self.settings.bullet_height))
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.carts.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        self.screen.blit(self.image, self.rect)