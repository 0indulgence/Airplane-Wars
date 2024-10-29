import pygame

#    管理爆炸效果
class Explosion(pygame.sprite.Sprite):

    def __init__(self, center):
        super().__init__()
        self.explosion_sm = []  # 存储爆炸效果的帧图像
        for i in range(9):
            filename = './resources/images/regularExplosion0{}.png'.format(i)  # 用f-string将文件名格式化，:04指定了宽度为4位数字，左侧以0补齐
            img = pygame.image.load(filename).convert()  # 载入图片，返回Surface对象，convert实现格式转换
            img.set_colorkey((0,0,0))   # 透明色
            img = pygame.transform.scale(img, (40, 40))     # 图片缩放
            self.explosion_sm.append(img)  # 将Surface对象添加到列表中备用

        pygame.sprite.Sprite.__init__(self)

        self.image = self.explosion_sm[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0      # 初始化帧数
        self.last_update = pygame.time.get_ticks()  # 记录上一次更新爆炸动画的时间
        self.frame_rate = 80  # 设定爆炸图片显示的间隔时间 ， 每隔80毫秒切换到下一帧的爆炸图像



    def update(self):
        now = pygame.time.get_ticks()  # 获取当前时间
        if now - self.last_update > self.frame_rate:  # 本帧与上一帧的时间差达到fram_rate时，显示1帧爆炸图片
            self.last_update = now  # 记录最近刷新时间
            self.frame += 1  # 帧数+1，这样下次才会调用下一张图片
            if self.frame == len(self.explosion_sm):  # 当爆炸图片到达最后一帧时，爆炸对象自杀(不再占用内存)
                self.kill()
            else:
                self.image = self.explosion_sm[self.frame]  # 指定要显示的爆炸图片(Surface对象)