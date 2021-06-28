class Settings:
    """A class to store settings for the game"""

    def __init__(self):
        """Initialize game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5