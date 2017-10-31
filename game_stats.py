class GameStats():

    """Track stats for alien invasion"""

    def __init__(self, settings):

        self.settings = settings
        self.reset_stats()
        self.game_active = False
        self.score = 0

        #high score will never be reset
        self.high_score = 0 

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
