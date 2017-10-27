import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, settings, screen, ship):
        """Creat a bullet object at the ships current position"""
        super().__init__()
        self.screen = screen

        #create a bullet surface at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the bullets position as a decimal
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def update(self):
        """Moves the bullet up the screen"""
        #update the position of the bullet
        self.y -= self.speed
        #update the rect position
        self.rect.y = self.y

    def draw_bullets(self):
        """Draw a bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
