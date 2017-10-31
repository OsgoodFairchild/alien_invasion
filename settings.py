class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the games settings"""

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230)

        #ship settings
        self.ship_limit = 3

        #bullet settings

        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_limit = 3

        #alien settings
        self.drop_speed = 10

        #game speed up
        self.speedup_scale = 1.5
        self.score_scale = 1.5

        self.inititialize_dynamic_settings()

    def inititialize_dynamic_settings(self):
        self.ship_speed = 10
        self.bullet_speed = 5
        self.alien_speed = 1
        self.fleet_direction = 5

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase_speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
