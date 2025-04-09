import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import CartBlaster


class CartArsenal:
    def __init__(self, game: 'CartBlaster'):
        self.game = game
        self.settings = game.settings
        self.blaster = pygame.sprite.Group()

    def update_blaster(self) -> None:
        self.blaster.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        for bullet in self.blaster.copy():
            if bullet.rect.bottom <= 0:
                self.blaster.remove(bullet)

    def draw(self) -> None:
        for bullet in self.blaster:
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.blaster) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.blaster.add(new_bullet)
            return True
        return False

