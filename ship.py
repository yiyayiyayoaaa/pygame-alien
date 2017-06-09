import pygame
from bullet import Bullet
import time


class Ship(object):
    def __init__(self, ai_settings, screen, bullets):
        self.screen = screen
        self.ai_settings = ai_settings
        self.bullets = bullets
        ship = pygame.image.load('image/rocket.png')
        self.image = pygame.transform.smoothscale(ship, (45, 45))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
        self.is_shoot = False

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

    def shoot(self):
        new_bullet = Bullet(self.ai_settings, self.screen, self, 0)
        self.bullets.add(new_bullet)
        print("发射子弹")

    def update(self, i):
        if self.is_shoot and i % 8 == 0:
            self.shoot()

        #for bullet in self.bullets.sprites():
        #   bullet.draw_bullet()
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_top and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        #self.update_bullets()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
