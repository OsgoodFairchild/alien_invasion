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

def create_fleet(settings, screen, ship, aliens):
    """Creates a fleet of aliens"""
    alien = Alien(settings, screen)
    number_aliens_x = get_number_of_aliens_x(settings, alien.rect.width)
    number_rows = get_number_of_rows(settings, ship.rect.height, alien.rect.height)

    #create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)

def get_number_of_aliens_x(settings, alien_width):
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_of_rows(settings, ship_height, alien_height):
    available_space_y = (settings.screen_height -
                        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
