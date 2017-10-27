import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship and its starting position on screen"""
        self.screen = screen

        #load the ship and get its rectangle object
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)
