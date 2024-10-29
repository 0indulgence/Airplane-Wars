import pygame
from pygame.sprite import Sprite
import math
#子弹类
clock = pygame.time.Clock()  #控制游戏循环中的帧率
class Bullet(Sprite):


    flag = 0
    flag2 = 0
    #在飞船所处的位置创建子弹
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # 先初始在（0,0）
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 子弹和飞船在一块
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color#子弹颜色
        self.speed_factor = ai_settings.bullet_speed_factor#子弹射速


    #向上移动子弹
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    #绘制子弹
    def draw_bullet(self):
        if Bullet.flag == 0 and Bullet.flag2 == 0:
            pygame.draw.rect(self.screen, self.color, self.rect)
        elif Bullet.flag > 0:
            # 加载图像
            self.bullet_image = pygame.image.load('./resources/images/love.png')
            # 绘制图像
            self.screen.blit(self.bullet_image, self.rect)
        else:
             # 加载图像
            self.bullet_image = pygame.image.load('./resources/images/shop04.png')
            self.bullet_image= pygame.transform.scale(self.bullet_image, (45, 30))  # 设置图片大小
            # 绘制图像
            self.screen.blit(self.bullet_image, self.rect)

class BossBullet(Sprite):
    """Boss发射的子弹"""

    def __init__(self, ai_settings, screen, bossalien, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(BossBullet, self).__init__()      #super(BossBullet, self)表示调用BossBullet类的父类的方法。调用父类的构造函数。
        self.screen = screen
        #射击目标（ship）
        self.target = ship.rect                 # 追踪
        # 在boss底部中央处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bossbullet_width,ai_settings.bossbullet_height)

        self.rect.x = bossalien.rect.centerx    #中心横坐标和底部纵坐标
        self.rect.y = bossalien.rect.bottom
        self.width = ai_settings.bossbullet_width
        self.height = ai_settings.bossbullet_height

        # 存储用小数表示的子弹位置
        self.y = float(bossalien.rect.bottom)

        self.y = bossalien.rect.bottom
        self.x = bossalien.rect.centerx

        self.color = ai_settings.bossbullet_color
    
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        clock.tick(60)      #控制游戏循环中的帧率
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.update(self.target, self.rect)
       
    def update(self,target,bossbullet):
        """自动瞄准"""
        speed = 5
        x1, y1 = bossbullet.x, bossbullet.y  # 追踪者（导弹）
        x2, y2 = self.target.center  # 目标（ship）
        dx = x2 - x1
        dy = y1 - y2
        r = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
        if r != 0:
            sin = dy / r
            cos = dx / r
            x1 += cos * speed
            y1 -= sin * speed
            bossbullet.x, bossbullet.y = x1, y1

            

    def reset_position(self, bossalien):
        """（当子弹飞出屏幕底部或者击中飞船时）回到开始的地方"""        #在哪里调用的
        self.y = bossalien.rect.bottom
        self.x = bossalien.rect.centerx
        # 更新rect位置
        self.rect.y = self.y
        self.rect.x = self.x
