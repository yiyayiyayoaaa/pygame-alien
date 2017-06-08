import pygame

from pygame.sprite import Sprite
from bullet import Bullet
import random


class Alien(Sprite):
    def __init__(self, ai_settings, screen, bullets):
        super(Alien, self).__init__()
        self.screen = screen
        self.bullets = bullets
        self.ai_settings = ai_settings
        img = random.choice(['image/alien1.png', 'image/alien2.png', 'image/alien3.png', 'image/alien4.png', 'image/alien5.png'])
        alien = pygame.image.load(img)
        self.image = pygame.transform.smoothscale(alien, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        new_bullet = Bullet(self.ai_settings, self.screen, self, 1)
        self.bullets.add(new_bullet)

    def shoot(self):
        new_bullet = Bullet(self.ai_settings, self.screen, self, 1)
        self.bullets.add(new_bullet)

    def update(self, i):
        if i % 72 == 0:
            self.shoot()
        self.y += self.ai_settings.alien_speed_factor
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
