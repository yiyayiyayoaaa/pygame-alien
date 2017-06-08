class Settings(object):
    '''存储所有设置的类'''
     # 定义画面帧率
    def __init__(self):
        '''初始化游戏的设置'''
        self.FRAME_RATE = 60
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 8

        self.bullet_speed_factor = 12
        self.bullet_speed_factor2 = 6
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255, 100, 100)

        self.alien_speed_factor = 4
