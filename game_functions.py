import sys
import pygame
from alien import Alien
from pygame.sprite import groupcollide
import random


def check_keydown_events(event, ai_settings, screen, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_top = True
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    elif event.key == pygame.K_SPACE:
        ship.is_shoot = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_top = False
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = False
    elif event.key == pygame.K_SPACE:
        ship.is_shoot = False


def check_play_button(state, play_button, mouse_x, mouse_y, aliens, ship, bullets, bullets2):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        state.game_active = True

        aliens.empty()
        bullets.empty()
        bullets2.empty()
        ship.center_ship()


def check_events(ai_settings, screen, ship, state, play_button, aliens, bullets, bullets2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(state, play_button, mouse_x, mouse_y, aliens, ship, bullets, bullets2)


def update_screen(ai_settings, screen, ship, aliens, bullets, bullets2, play_button, game_state):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in bullets2.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not game_state.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    pygame.sprite.groupcollide(bullets, aliens, True, True)


def update_bullets2(ship, bullets, state):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.top >= ship.ai_settings.screen_height:
            bullets.remove(bullet)
    if pygame.sprite.spritecollideany(ship, bullets):
        state.game_active = False


def update_aliens(aliens, ship, i, state):
    aliens.update(i)
    if pygame.sprite.spritecollideany(ship, aliens):
        state.game_active = False


def create_alien(ai_settings, screen, aliens, bullets):
    alien = Alien(ai_settings, screen, bullets)
    screen_width = ai_settings.screen_width
    alien.x = random.choice([x for x in range(screen_width-50)])
    alien.rect.x = alien.x
    aliens.add(alien)
