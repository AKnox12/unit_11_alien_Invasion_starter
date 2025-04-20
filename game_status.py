# Lab 13_Knox12_2
# Python
# Autumn Knox
# Configuring in Python a simple game to shoot falling rocks from a cart.
# 04/13/2025

from pathlib import Path
import json


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import CartBlaster

class GameStats():

    def __init__(self, game) -> None:
        """Starting point of the game."""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """Score's file and boundaries"""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 80:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.high_score = scores.get('high_scores', 0)
        else:
            self.high_score = 0
            self.save_scores()

    def save_scores(self):
        scores = {
            'high_scores': self.high_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Cannot Be Found: {e}')
 

    def reset_stats(self):
        """Settings that will change as the game progresses"""
        self.ship_left = self.settings.starting_carts_count
        self.score = 0
        self.level = 1 

    def update(self, collisions):
       """Update the scores"""
       self._update_score(collisions)
       self._update_max_score()
       self._update_high_score()

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
        
    def _update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        
    def _update_score(self, collisions):
        for rocks in collisions.values():
            self.score += self.settings.rocks_points


    def update_level(self) -> None:
        self.level += 1
        #print(self.level)

    

