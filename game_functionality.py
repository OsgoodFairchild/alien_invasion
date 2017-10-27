import sys, pygame

from alien  import Alien
from bullet import Bullet

def check_events(settings, screen, ship, bullets):
    #watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #move ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(screen, settings, ship, bullets, aliens):
    screen.fill(settings.screen_color)

    #redraw all the bullets behind the ship
    for bullet in bullets.sprites():
        bullet.draw_bullets()

    ship.blitme()
    aliens.draw(screen)
    #make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """Update the position of the bullet and delete bullets that have gone off screen"""
    bullets.update()

    #Get rid of bullets that have dissapeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        #print(len(bullets))

def fire_bullets(settings, screen, ship, bullets):
    #create a new bullet and add it to the group bullets
    if len(bullets) < settings.bullet_limit:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(settings, screen, aliens):
    """Creates a fleet of aliens"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    #create the first row of aliens
    for alien_number in range(number_aliens_x):
        #create an alien and place it in the row
        alien = Alien(settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
