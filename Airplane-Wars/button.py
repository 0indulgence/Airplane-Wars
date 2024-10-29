import pygame.font

class Button():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()        #用来表示整个游戏窗口的位置和大小

        # 设置按钮属性
        self.width, self.height = 200, 50
        self.button_color = (90, 200, 30)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
      
    #加载文字
    def prep_text(self, stats):
        if not stats.game_active and not stats.game_paused and not stats.game_ended:
            self.msg = 'Play!'
        elif stats.game_active and stats.game_paused:
            self.msg = 'Resume'
        elif stats.game_ended:
            self.msg = 'Try Again!'

    # 加载标签
    def prep_msg(self, stats):

        self.prep_text(stats)   #加载文字
        #将存储在msg中的文本转换为图像
        self.msg_image = self.font.render(self.msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    # 绘制一个用颜色填充的按钮，再绘制文本
    def draw_button(self, stats):

        # 加载图像
        self.button_image = pygame.image.load('./resources/images/begin.png')
        self.button_image = pygame.transform.scale(self.button_image, (self.width, self.height))
        # 绘制图像
        self.screen.blit(self.button_image, self.rect)



class Shop_Button:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()        #用来表示整个游戏窗口的位置和大小

        # 设置按钮属性
        self.width, self.height = 100, 50
        self.button_color = (90, 200, 30)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx + 200
        self.rect.centery = self.screen_rect.centery - 200


    def draw_button(self):


        # 加载图像
        self.button_image = pygame.image.load('./resources/images/shop.png')
        self.button_image = pygame.transform.scale(self.button_image, (self.width, self.height))
        # 绘制图像
        self.screen.blit(self.button_image, self.rect)


class double_play_Button:

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()        #用来表示整个游戏窗口的位置和大小

        # 设置按钮属性
        self.width, self.height = 200, 50
        self.button_color = (90, 200, 30)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.centery = self.screen_rect.centery + 80

        self.player_flag = 0 #两个飞机

    # 加载标签
    def prep_msg(self, stats):

        #将存储在msg中的文本转换为图像
        self.msg_image = self.font.render(self.msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    # 绘制一个用颜色填充的按钮，再绘制文本
    def draw_button(self, stats):
        # 加载图像
        self.button_image = pygame.image.load('./resources/images/double_player.png')
        self.button_image = pygame.transform.scale(self.button_image, (self.width, self.height))
        # 绘制图像
        self.screen.blit(self.button_image, self.rect)


class Owner_Button:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()        #用来表示整个游戏窗口的位置和大小

        # 设置按钮属性
        self.width, self.height = 50, 50
        self.button_color = (90, 200, 30)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx +200
        self.rect.centery = self.screen_rect.centery -150

    def draw_button(self):


        # 加载图像
        self.button_image = pygame.image.load('./resources/images/help.png')
        self.button_image = pygame.transform.scale(self.button_image, (self.width, self.height))
        # 绘制图像
        self.screen.blit(self.button_image, self.rect)