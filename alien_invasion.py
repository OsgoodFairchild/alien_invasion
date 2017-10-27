import pygame

from settings import Settings
from ship import Ship
import game_functionality as gf

def run_game():
    #Initialize game and create a screen object
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    #start the main loop for the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(screen, settings, ship)

run_game()
