import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Base class, what managing resources and behavior of game"""

    def __init__(self):
        """Initialization game, creating resources"""
        pygame.init()

        # create settings obj
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # malen the ship
        self.ship = Ship(self)

        # Set bkg color
        self.bg_color = (230, 230, 230)

    def _check_events(self):
        # Look for the moving mouse or click on the buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # update screen
        # refresh bkg
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Display the last screen
        pygame.display.flip()

    def run_game(self):
        """Start main cycle of game"""
        while True:
            self._check_events()
            self._update_screen()


if __name__ == '__main__':
    """Create and run game"""
    ai = AlienInvasion()
    ai.run_game()