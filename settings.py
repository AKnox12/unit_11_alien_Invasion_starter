from pathlib import Path
class Settings:
    '''A class to stor all the settings for ALien Invasion'''

    def __init__(self):
        '''Initialize the game's settings.'''
        # Screen Settings
        self.name: str = "Cart Blaster"
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'cavern.png'


        self.cart_file = Path.cwd() / 'Assets' / 'images' / 'cart.png'
        self.cart_width = 170
        self.cart_height = 190
        self.carts_speed = 5

        self.bullet_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'beams.png'
        self.laser_sound = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_width = 25
        self.bullet_height = 80
        self.bullet_amount = 7
        