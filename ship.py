import pygame

class Ship:
    """class for managing the ship"""

    def __init__(self, ai_game):
        """initialisation and set first position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # download pic of the ship and get her rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Create even new ship in bottom of the screen in center
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """намалювати корабель у його поточному розташуванні"""
        self.screen.blit(self.image, self.rect)
