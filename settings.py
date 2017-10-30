class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the games settings"""

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 10
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 10
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_limit = 5

        #alien settings
        self.alien_speed = 1
        self.drop_speed = 10
        self.fleet_direction = 5
