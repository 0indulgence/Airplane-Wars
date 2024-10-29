import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    #飞船初始化
    def __init__(self, ai_settings, screen):
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        #上传飞船图片并获取其外接矩阵
        self.image = pygame.image.load('./resources/images/ship5.png')
        self.image = pygame.transform.scale(self.image, (80, 80))  # 设置图片大小
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        #把每艘新飞船放在屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 5

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        #自动射击
        self.shoot_type = 1#奇数手动射击，偶数自动射击

    def update(self):
        #控制飞船位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor#向右

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor#向左

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor #向下

        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor #向上

        self.rect.centerx = self.center
        self.rect.centery = self.centery

    #让飞船居中
    def center_ship(self):
        self.center = self.screen_rect.centerx

    #在指定位置绘制飞船
    def blitme(self):
        self.screen.blit(self.image, self.rect)
