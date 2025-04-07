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
        self.bg_file = Path.cwd() /'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'Carles_bad_cavern_3.png'