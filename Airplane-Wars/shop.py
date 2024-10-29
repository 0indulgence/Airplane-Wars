import pygame

class Shop:
    def __init__(self,ai_settings):
        
        # 屏幕设置
        self.screen_width = 500
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width , self.screen_height ))  # 屏幕大小


        self.player_coins = 500
        # 退出按钮
        self.exit_button = pygame.Rect(10, 10, 50, 30)
        self.exit_button_color = (255, 0, 0)
        self.draw(self.screen,ai_settings)
        self.flag = 0

    # 屏幕设置
    def draw(self,screen,ai_settings):

        # 绘制商店界面的文本或图像
        font = pygame.font.Font(None, 36)  # 创建字体对象，可以根据需要更改字体和大小
        text = font.render("Welcome to the Shop", True, (255, 255, 255))  # 创建文本对象，可以根据需要更改文本和颜色
        text_rect = text.get_rect()
        text_rect.midtop = self.screen.get_rect().midtop  # 将文本放置在屏幕正上方
        text_rect.y += 100  # 向下平移100个单位
        self.screen.blit(text, text_rect)  # 在屏幕上绘制文本



         # 绘制退出按钮
        self.exit_button.width = 65  # 修改按钮的宽度
        self.exit_button.height = 40  # 修改按钮的高度 
        filename = './resources/images/shop_quit.png'
        shop_quit = pygame.image.load(filename).convert()
        shop_quit = pygame.transform.scale(shop_quit, (self.exit_button.width, self.exit_button.height))
    
        screen.blit(shop_quit,( 10,  5))

        # 绘制商品图片和购买按钮
        x_position = 50
        y_position = 150
        button_width = 120
        button_height = 40
        button_color = (0, 255, 0)
 
        filename = './resources/images/shop01.jpg'
        item_image = pygame.image.load(filename).convert()
        item_image = pygame.transform.scale(item_image, (150, 150))
        screen.blit(item_image, (x_position, y_position))

        # 绘制购买按钮
        self.button_rect = pygame.Rect(x_position + 10, y_position + item_image.get_height() + 10, button_width, button_height)
 
        filename = './resources/images/shop03.png'
        shop_button1 = pygame.image.load(filename).convert()
        shop_button1 = pygame.transform.scale(shop_button1, ( button_width, button_height))
        screen.blit(shop_button1,self.button_rect)
        

        x_position += item_image.get_width() + 50

        filename = './resources/images/shop08.png'
        item_image = pygame.image.load(filename).convert()
        item_image = pygame.transform.scale(item_image, (150, 150))
        screen.blit(item_image, (x_position, y_position))

        # 绘制购买按钮
        self.button_rect_2 = pygame.Rect(x_position + 10, y_position + item_image.get_height() + 10, button_width, button_height)
        pygame.draw.rect(screen, button_color, self.button_rect_2)
        filename = './resources/images/shop03.png'
        shop_button2 = pygame.image.load(filename).convert()
        shop_button2 = pygame.transform.scale(shop_button2, ( button_width, button_height))
        screen.blit(shop_button2,self.button_rect_2)

        x_position = 50
        y_position = 400
        filename = './resources/images/shop10.jpg'
        item_image = pygame.image.load(filename).convert()
        item_image = pygame.transform.scale(item_image, (150, 150))
        screen.blit(item_image, (x_position, y_position))

        # 绘制购买按钮
        self.button_rect_3 = pygame.Rect(x_position + 10, y_position + item_image.get_height() + 10, button_width, button_height)
 
        filename = './resources/images/shop03.png'
        shop_button1 = pygame.image.load(filename).convert()
        shop_button1 = pygame.transform.scale(shop_button1, ( button_width, button_height))
        screen.blit(shop_button1,self.button_rect_3)

        x_position += item_image.get_width() + 50

        filename = './resources/images/shop07.jpg'
        item_image = pygame.image.load(filename).convert()
        item_image = pygame.transform.scale(item_image, (150, 150))
        screen.blit(item_image, (x_position, y_position))

        # 绘制购买按钮
        self.button_rect_4 = pygame.Rect(x_position + 10, y_position + item_image.get_height() + 10, button_width, button_height)
        pygame.draw.rect(screen, button_color, self.button_rect_4)
        filename = './resources/images/shop03.png'
        shop_button2 = pygame.image.load(filename).convert()
        shop_button2 = pygame.transform.scale(shop_button2, ( button_width, button_height))
        screen.blit(shop_button2,self.button_rect_4)
        # 刷新屏幕显示
        pygame.display.flip()
#########################################################################################################
        

    # 以下是后续想法，还未实现

    def display_items(self):
        pygame.init()
        screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Shop")
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 24)
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            screen.fill((255, 255, 255))
            coins_text = font.render("Coins: {}".format(self.player_coins), True, (0, 0, 0))
            screen.blit(coins_text, (10, 10))
            y = 50
            for item_id, item_info in self.items.items():
                item_text = font.render("{} - Price: {} coins".format(item_info['name'], item_info['price']), True, (0, 0, 0))
                screen.blit(item_text, (10, y))
                y += 30
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def purchase_item(self, item_id):
        if item_id in self.items:
            item_info = self.items[item_id]
            if self.player_coins >= item_info['price']:
                self.player_coins -= item_info['price']
                print("You purchased {} for {} coins.".format(item_info['name'], item_info['price']))
                # 在这里添加适当的代码来处理购买后的效果
            else:
                print("Insufficient coins. You cannot purchase this item.")
        else:
            print("Invalid item ID. Please select a valid item.")

    # 在这里添加打开商店界面的代码
    def open_shop():
        print("Opening shop...")

