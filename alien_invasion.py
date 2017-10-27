import sys, pygame

from settings import Settings
from ship import Ship

def run_game():
    #Initialize game and create a screen object
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    #start the main loop for the game
    while True:

        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(settings.screen_color)
        ship.blitme()

        #make the most recently drawn screen visible
        pygame.display.flip()

run_game()
