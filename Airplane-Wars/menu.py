import pygame.font
from button import *
from shop import Shop

class Menu():

    def __init__(self, ai_settings, screen, stats ):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 尺寸颜色
        self.width = 600
        self.height = 300
        self.bg_color = (128, 128, 128,250)
        self.text_color = (255, 255, 255)
        self.font1 = pygame.font.SysFont(None, 50)
        self.font = pygame.font.SysFont(None, 40)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center  #游戏窗口在屏幕上居中显示
        self.owner_button = Owner_Button(self.screen)
        self.prep_msg(stats)

        #创建按钮
        self.play_button = Button(ai_settings, screen, stats)
        self.double_play_button = double_play_Button(ai_settings, screen, stats)
        self.shop_button = Shop_Button(ai_settings, self.screen)
        
    def prep_text(self, stats):
        #游戏初始界面
        if not stats.game_active and not stats.game_paused and not stats.game_ended:
            self.msg = 'Alien Invasion'
        #暂停
        elif stats.game_active and stats.game_paused:
            self.msg = 'Pause'
        #游戏结束
        elif stats.game_ended:
            self.msg = 'Gameover'

    def prep_msg(self, stats):
        self.prep_text(stats)
        # 和botton的保持一致
        self.msg_image = self.font1.render(self.msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center
        # 布局
        self.msg_image_rect.y = self.rect.center[1] - (110 if stats.game_ended else 70)
        #起始页面和暂停界面
    
        if stats.game_ended:
            self.prep_score_msg(stats)#得分信息

    #载入得分信息
    def prep_score_msg(self, stats):
        rounded_score = int(round(stats.score, -1)) # 浮点数取整
        score_str = str(f'{rounded_score:,}')   # 得分转化为字符串
        self.score_msg = f'Your score: {score_str}' # 存储显示玩家得分的文本
         # 和botton的保持一致
        self.score_msg_image = self.font.render(
            self.score_msg, True, self.text_color, self.bg_color)
        self.score_msg_image_rect = self.score_msg_image.get_rect()
        self.score_msg_image_rect.center = self.rect.center
         # 布局
        self.score_msg_image_rect.y = (self.rect.center[1] - 60)

    #绘制得分菜单
    def draw_menu(self, stats):

            # 加载菜单背景图像
        menu_bg_image = pygame.image.load('./resources/images/menu.png')
        menu_bg_image = pygame.transform.scale(menu_bg_image, (self.width, self.height))

        self.prep_msg(stats)
        self.screen.blit(menu_bg_image, (0, 200))  # 绘制菜单背景图像

        self.screen.blit(self.msg_image, self.msg_image_rect)

        #按钮
        self.play_button.draw_button(stats)
        self.double_play_button.draw_button(stats)
        self.shop_button.draw_button()

               # 联系客服
        self.owner_button.draw_button()