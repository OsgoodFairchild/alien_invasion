import pygame

from alien      import Alien
from settings   import Settings
from ship       import Ship
from game_stats import GameStats
from button     import Button
from pygame.sprite import Group
import game_functionality as gf

def run_game():
    #Initialize game and create a screen object
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #make a play button
    play_button = Button(settings, screen, "Play")

    stats = GameStats(settings)

    alien = Alien(settings, screen)
    ship = Ship(settings, screen)

    #make a group to store aliens in
    aliens = Group()
    gf.create_fleet(settings, screen, ship, aliens)

    #make a group to store bullets in
    bullets = Group()

    #start the main loop for the game
    while True:
        gf.check_events(settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, ship, aliens, bullets)
            gf.update_aliens(settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(stats, screen, settings, ship, bullets, aliens, play_button)

run_game()
