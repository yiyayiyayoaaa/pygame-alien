import pygame

from setting import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from pygame.locals import *


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()
    bullets = Group()
    bullets2 = Group()
    aliens = Group()
    ship = Ship(ai_settings, screen, bullets)
    #ship_shoot_thread = threading.Thread(target=show_bullets,args=(ship,))
    # 开始游戏的主循环
    i = 72
    #alien = Alien(ai_settings, screen)
    while True:       
        # 监听键盘和鼠标事件
        clock.tick(ai_settings.FRAME_RATE)
        gf.check_events(ai_settings, screen, ship)
        # 每次循环都重绘屏幕, 让最近绘制的屏幕可见
        ship.update(i)
        gf.update_bullets(aliens, bullets)
        gf.update_bullets2(ship, bullets2)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, bullets2)
        gf.update_aliens(aliens, ship, i)
        if i == 72:
            gf.create_alien(ai_settings, screen, aliens, bullets2)
            i = 0
        i += 1

if __name__ == '__main__':
    run_game()
