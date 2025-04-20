# Lab 13_Knox12_2
# Python
# Autumn Knox
# Configuring in Python a simple game to shoot falling rocks from a cart.
# 04/13/2025

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import CartBlaster

class GameStats():

    def __init__(self, game) -> None:
        """Starting point of the game."""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self):
        """Settings that will change as the game progresses"""
        self.ship_left = self.settings.starting_carts_count
        self.score = 0
        self.level = 1 

    def update(self, collisions):
       # update score
       self._update_score(collisions)
       self._update_max_score()

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f'Max: {self.max_score}')

        #update max_score


    def _update_score(self, collisions):
        for rocks in collisions.values():
            self.score += self.settings.rocks_points
        #print(f"Basic: {self.score}")


    def update_level(self) -> None:
        self.level += 1
        #print(self.level)

    

