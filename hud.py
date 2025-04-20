import pygame.font
#from typing import TYPE_CHECKING
#from alien_invasion import CartBlaster

#if TYPE_CHECKING:


class HUD:

    def __init__(self, game: 'CartBlaster') -> None:
        """Display of the data, and any updates of images"""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file,
            self.settings.HUD_font_size)
        self.padding = 20
        self._setup_life_image()
        self.update_scores()

    def _setup_life_image(self) -> None:
        self.life_image = pygame.image.load(self.settings.cart_file)
        self.life_image = pygame.transform.scale(self.life_image, (
            self.settings.cart_width, self.settings.cart_height
            ))
        self.life_rect = self.life_image.get_rect()



    def update_scores(self) -> None:
        """Update for score in the game"""
        self._update_max_score()
        self._update_score()
        self._update_high_score()
        self._update_level()

        
    def _update_score(self):
        """Score in the game"""
        score_str = f'Score: {self.game_stats.score: .0f}'
        self.score_image = self.font.render(score_str, True,
            self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_max_score(self):
        """Max score in the game"""
        max_score_str = f'Max-Score: {self.game_stats.max_score: .0f}'
        self.max_score_image = self.font.render(max_score_str, True,
            self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_high_score(self):
        """High score in the game"""
        high_score_str = f'High-Score: {self.game_stats.high_score: .0f}'
        self.high_score_image = self.font.render(high_score_str, True,
            self.settings.text_color, None)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.midtop = (self.boundaries.centerx,self.padding)

    def _update_level(self):
        """Level in the game"""
        level_str = f'Level: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True,
            self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding

    def _draw_lives(self) -> None:
        current_x = self.padding
        current_y = self.padding
        for _ in range(self.game_stats.cart_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding


    def draw(self):
        """Drawing out the scores into the game"""
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.max_score_image,self.max_score_rect)
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self._draw_lives()
