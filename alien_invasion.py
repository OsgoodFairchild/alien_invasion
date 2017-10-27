import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functionality as gf

def run_game():
    #Initialize game and create a screen object
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(settings, screen)
    #make a group to store bullets in
    bullets = Group()

    #start the main loop for the game
    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(screen, settings, ship, bullets)

run_game()
