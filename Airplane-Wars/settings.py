import pygame
from button import *
# 设置类
class Settings():

    # 游戏初始设置
    def __init__(self):
####################################################################################################################

        # 屏幕设置

        self.background = pygame.image.load('./resources/images/background_1.png')
        self.screen_width = 500
        self.screen_height = 700

        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height)) # 设置图片大小
####################################################################################################################

        # 音量设置
        self.high_volume = 10
        self.med_volume = 10
        self.low_volume = 10

####################################################################################################################
        # 血量
        self.ship_limit = 5
####################################################################################################################
        
        # 子弹设置
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (0, 0, 255)

####################################################################################################################
        # 屏幕上最多同时存在的子弹数
        self.bullets_allowed = 10
####################################################################################################################
        
        # boss子弹
        self.bossbullet_width = 10
        self.bossbullet_height = 10
        self.bossbullet_color = (255, 0, 0)
        self.bossbullets_allowed = 3

        # boss 移动速度
        self.bossalien_direction = 1

        # 每过一关，加快游戏节奏
        self.alien_speed_scale = 1.5
        self.ship_speed_scale = 1.5
        self.alien_score_multiplier = 1.5  # 每轮外星人分数提高倍数

        # 活动属性初始化
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        # 速度因子
        self.ship_speed_factor = 4
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 2
        self.bossalien_points = 500

    # 提高速度设置
    def increase_speed(self):
        self.ship_speed_factor *= self.ship_speed_scale
        # self.bullet_speed_factor *= self.ship_speed_scale
        self.alien_speed_factor *= self.alien_speed_scale
        self.alien_score_multiplier += 0.1
