import sys, pygame

from alien  import Alien
from bullet import Bullet
from time   import sleep

def ship_hit(settings, stats, screen, ship, aliens, bullets):

    if stats.ships_left >= 0:
        stats.ships_left -= 1

        #empty the lists of aliens and bullets
        aliens.empty()
        bullets.empty()

    #create a new fleet and center the ship
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

    #pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_events(settings, screen, stats, play_button, ship, aliens, bullets):
    #watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, play_button, ship, aliens, bullets,  mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_play_button(settings, screen, stats, play_button, ship, aliens, bullets,  mouse_x, mouse_y):
    """Start a new game when play is selected"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not stats.game_active:
            pygame.mouse.set_visible(False)
            stats.reset_stats()
            stats.game_active = True

            #empty aliens and bullets list
            aliens.empty()
            bullets.empty()

            #create a new fleet and center the ship
            create_fleet(settings, screen, ship, aliens)
            ship.center_ship()

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

def update_screen(stats, screen, settings, ship, bullets, aliens, play_button):
    screen.fill(settings.screen_color)

    #redraw all the bullets behind the ship
    for bullet in bullets.sprites():
        bullet.draw_bullets()

    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()
    #make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(settings, screen, ship, aliens, bullets):
    """Update the position of the bullet and delete bullets that have gone off screen"""
    bullets.update()

    #Get rid of bullets that have dissapeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        #print(len(bullets))
    check_bullet_alien_collisions(settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)

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

def update_aliens(settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)
        check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.drop_speed
    settings.fleet_direction *= -1

def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
    """check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets)
            break
