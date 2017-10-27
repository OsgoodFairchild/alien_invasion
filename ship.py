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

        #ship movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships movement based off the flags"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)
