# Lab 13_Knox12_2
# Python
# Autumn Knox
# Configuring in Python a simple game to shoot falling rocks from a cart.
# 04/13/2025

from pathlib import Path
class Settings:
    '''A class to stor all the settings for ALien Invasion'''

    def __init__(self):
        '''Initialize the game's settings.'''
        """Main file settings and Screen Settings"""
        self.name: str = "Cart Blaster"
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'cavern.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'file' / 'scores.json'

        """Carts settings"""
        self.cart_file = Path.cwd() /'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'cart.png'
        self.cart_width = 170
        self.cart_height = 190

        """Bullet settings and images"""
        self.bullet_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'laser_beams.png'
        self.laser_sound = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'sound' / 'Beam_sound.mp3'
        self.impact_sound = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'sound' / 'impactSound.mp3'


        """Rocks Settings and image"""
        self.rocks_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'Asteroid Brown.png'
        self.rocks_width = 40
        self.rocks_height = 40
        self.fleet_direction = 1

        """Button settings and text"""
        self.button_width = 200
        self.button_height = 50
        self.button_color = (245, 10, 25)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'Fonts' / 'VT323' / 'VT323-Regular.ttf'
    

    def initialize_dynamic_settings(self):
        """dynamic settings like speeds go here."""
        self.carts_speed = 5
        self.starting_carts_count = 3

        self.bullet_width = 25
        self.bullet_height = 80
        self.bullet_speed = 7
        self.bullet_amount = 7

        self.fleet_speed = 3
        self.fleet_drop_speed = 20
        self.rocks_points = 50

    def increase_difficulty(self) -> None:
        """Difficulty increase funtion"""
        self.carts_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
