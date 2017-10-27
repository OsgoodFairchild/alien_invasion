class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the games settings"""

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 5

        #bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_limit = 5
        
