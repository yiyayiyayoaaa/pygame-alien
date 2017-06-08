import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """docstring for Bullet"""
    def __init__(self, ai_settings, screen, ship, type):
        super(Bullet, self).__init__()
        self.screen = screen
        self.type = type
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        if type == 0:
            self.rect.top = ship.rect.top
            self.speed_factor = ai_settings.bullet_speed_factor
        else:
            self.rect.bottom = ship.rect.bottom
            self.speed_factor = ai_settings.bullet_speed_factor2
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color

    def update(self):
        if self.type == 0:
            self.y -= self.speed_factor
        else:
            self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
