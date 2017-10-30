import pygame

class Ship():

    def __init__(self, settings, screen):
        """Initialize the ship and its starting position on screen"""
        self.screen = screen
        self.settings = settings

        #load the ship and get its rectangle object
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #ship center stored as decimal
        self.center = float(self.rect.centerx)

        #ship movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships movement based off the flags"""
        #update the ships center value not the container
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed

        #update rect container from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center the ship on the screen"""
        self.center = self.screen_rect.centerx
