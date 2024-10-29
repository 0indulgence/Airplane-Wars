import pygame
import random
from pygame.sprite import Sprite
from random import randint


# 普通外星人类
class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        # 初始化外星人和定义起始位置
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.ai_settings = ai_settings
        # 上传外星人图片
        self.image = pygame.image.load(self.get_color())  # 根据颜色选图片
        self.image = pygame.transform.scale(self.image, (60, 60))  # 设置图片大小
        self.image2 = self.image.copy()
      
        # 定义外星人位置（最初都在左上角）
        self.rect = self.image2.get_rect()
        self.rect.x = self.rect.width + 200
        self.rect.y = 0

        # 存储准确位置
        self.x = float(self.rect.x)
        self.fleet_direction = 1  # 设置外星人群左右移动方向
        self.fleet_drop_speed = 10  # 外星人群向下移动速度

        #外星人速度
        self.speedy = random.randrange(1, 2)
        self.speedx = random.randrange(-3, 3)

        #生命
        self.health  = 0

    #     #外星人旋转
    #     self.rot = 0  #旋转角度
    #     self.rot_speed = random.randrange(-8, 8)
    #     self.last_update = pygame.time.get_ticks()

    # # 实现外星人在空中的旋转
    # def rotate(self):
    #     now = pygame.time.get_ticks()  #获得时间戳，计算时间差
    #     if now - self.last_update > 50:
    #         self.last_update = now
    #         self.rot = (self.rot + self.rot_speed) % 360
    #         new_image = pygame.transform.rotate(self.image,self.rot)  #旋转
    #         old_center = self.rect.center

    #         #更新图片和边界
    #         self.image2 = new_image
    #         self.rect = self.image2.get_rect()
    #         #保证中心对齐
    #         self.rect.center = old_center

    # 使得外星人降落方式随机化
    def update(self):
################################################################
        # self.rotate()
################################################################
        self.rect.x += (self.speedx * self.fleet_direction)
        self.rect.y += self.speedy

    # 判断外星人是否在屏幕边缘
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True

        elif self.rect.left <= 0:
            return True

    # 设置外星人颜色
    def get_color(self):
        colors = ['./resources/images/tqld.png', './resources/images/sgls.png', './resources/images/nsk.png']
        random_index = randint(0, len(colors) - 1)

        #设置颜色和得分
        alien_color = colors[random_index]
        self.set_alien_points(alien_color)
        return alien_color

    # 不同颜色外星人得分不一样
    def set_alien_points(self, color):
        if color == './resources/images/nsk.png':
            self.points = 10
            self.health = 1
        elif color == './resources/images/tqld.png':
            self.points = 15
            self.health = 2
        elif color == './resources/images/sgls.png':
            self.points = 20
            self.health = 3

    # 在指定位置绘制外星人
    def blitme(self):
        self.screen.blit(self.image2, self.rect)  #pygame


class BossAlien(Sprite):
    """Boss"""

    def __init__(self, ai_setting, screen, health=500):
        """初始化外星人并设置其起始位置"""
        self.screen = screen
        self.ai_settings = ai_setting
        self.health = health

        # 加载Boss外星人图像，并设置其rect属性
        self.image = pygame.image.load('./resources/images/pn1.png')
        self.image = pygame.transform.scale(self.image, (200, 170))  # 设置图片大小
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = 343-120
        self.rect.y = 100

        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        
        self.speedx = random.randrange(-4, 4,2)


    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def draw_health_bar(self, screen):

        """显示血条"""
        # 参数依次表示：在SCREEN上面绘制，颜色，（该图案左上角的坐标，长度和高度）

        # 空白血条pygame.draw.rect(surface, color, rect, width)

        pygame.draw.rect(screen, (0, 255, 0), ((93, 100), (500, 10)))  #绿血条
        
        # 红色的现有血量
        pygame.draw.rect(screen, (255, 0, 0), ((93, 100), (self.health, 10)))

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左或向右移动外星人"""
        self.rect.x += (self.speedx * self.ai_settings.bossalien_direction)  # 未设置纵向移动

