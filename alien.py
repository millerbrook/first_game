import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initializing the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen