import pygame

class Carts:
    '''a class to manage the cart.'''

    def __init__(self, ai_game):
        '''Initiate the cart and set the starting position.'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the Cart image and get rect.
        self.image = pygame.image.load('image/cart.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        

    def blitme(self):
        '''Draw the cart at its current location.'''
        self.screen.blit(self.image, self.rect)
        