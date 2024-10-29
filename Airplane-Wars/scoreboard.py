import pygame.font
from pygame.sprite import Group
from ship import Ship
from button import *

#记分牌
class Scoreboard():

    def __init__(self, ai_settings, screen, stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (226, 188, 0)
        self.font = pygame.font.SysFont(None, 40)
        self.font2 = pygame.font.SysFont(None, 30)

        self.prep_images()

    def prep_score(self):
        #将“得分”转换为渲染的图像
        rounded_score = int(round(self.stats.score, -1))
        self.score_image = self.font2.render(str(rounded_score), True, self.text_color)

        # 得分放在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
              # 加载图像
        self.score_image_2 = pygame.image.load('./resources/images/score.png')
        self.score_image_2 = pygame.transform.scale(self.score_image_2, (80,30))
        self.score_image_rect = self.score_image_2.get_rect()
        self.score_image_rect.right = self.score_rect.left - 10  # 设置图像的右边缘与文字的左边缘对齐
        self.score_image_rect.centery = self.score_rect.centery

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        
        self.high_score_image = self.font.render(str(high_score), True, (255,255,0))
        # 最高分放在顶部中间
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

        # 加载图像
        self.button_image = pygame.image.load('./resources/images/highest.png')
        self.button_image = pygame.transform.scale(self.button_image, (100,30))
        self.button_image_rect = self.button_image.get_rect()
        self.button_image_rect.right = self.high_score_rect.left - 10  # 设置图像的右边缘与文字的左边缘对齐
        self.button_image_rect.centery = self.high_score_rect.centery



#############################################################################

    def prep_level(self):
        self.level_image = self.font2.render('LEVEL:'+str(self.stats.level), True, self.text_color)

        # 等级放在得分下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        #显示剩余生命
        self.ships = Group()    # 存储飞船对象的群组
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10
            ship.rect.y = 10 + (ship_number * (ship.rect.height + 3))
            self.ships.add(ship)

#############################################################################
    def prep_images(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.shop_button = Shop_Button(self.ai_settings, self.screen)

#############################################################################

    def show_score(self):
        
        #绘制飞船
        self.ships.draw(self.screen)    #未找到在哪里

        # 绘制按钮
        # self.shop_button.draw_button()
        
        #显示得分
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.score_image_2, self.score_image_rect)

        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.button_image, self.button_image_rect)

        self.screen.blit(self.level_image, self.level_rect)



  




