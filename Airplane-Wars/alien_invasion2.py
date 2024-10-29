import pygame
from pygame.sprite import Group
import time
import alien
from settings import Settings
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from menu import Menu
from ship import Ship
from alien import *
from bullet import *
from shop import Shop
from button import *

def run_game():
    # 初始化游戏并创建游戏资源
    pygame.init()

    # 初始化setting类
    ai_settings = Settings()

    # 设置游戏进程
    stats = GameStats(ai_settings)

    # 设置屏幕
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

       
    pygame.display.set_caption('Alien Invasion')
    
    # 设置记分牌
    scoreboard = Scoreboard(ai_settings, screen, stats)
 
    # 开始按钮菜单
    menu = Menu(ai_settings, screen, stats)

    # 飞船、外星人、子弹
    ship = Ship(ai_settings, screen)
    ship2 = Ship(ai_settings, screen)
    # ship2 = ship
    aliens = Group()
    bullets = Group()
    bullets2 = Group()
    bossalien = BossAlien(ai_settings, screen)
    bossbullet = BossBullet(ai_settings, screen, bossalien, ship)
    all_sprites = pygame.sprite.Group()

    # 外星舰队  
    gf.create_fleet(ai_settings, screen, ship, aliens,stats)
    # 控制自动射速
    i = 0
    # 主循环
    while True:
        #控制射速
        i += 1
        i = i % 10

        gf.check_events(ai_settings, screen, stats, scoreboard, menu, ship,ship2, aliens, bullets,menu.shop_button)

        # 过关
        if stats.game_active and not stats.game_paused:
            ship.update()
            ship2.update()
            gf.update_bullets(ai_settings, screen, stats, scoreboard, menu, ship, aliens, bullets, bossalien, bossbullet,all_sprites)
            gf.update_bullets(ai_settings, screen, stats, scoreboard, menu, ship2, aliens, bullets2, bossalien, bossbullet,all_sprites)
            gf.update_aliens(ai_settings, stats, scoreboard, menu,screen, ship,ship2, aliens, bullets, bossalien, bossbullet,all_sprites)
            
            #偶数 自动
            if menu.double_play_button.player_flag == 0:
                if ship.shoot_type%2==0 and i == 0:
                    gf.fire_bullet(ai_settings, screen, ship, bullets) 

                    
            elif ship.shoot_type%2==0 and i == 0:
                gf.fire_bullet(ai_settings, screen, ship, bullets)
                gf.fire_bullet(ai_settings, screen, ship2, bullets)

        if menu.double_play_button.player_flag == 0:
            gf.update_screen(ai_settings, screen, stats, scoreboard, ship, ship,aliens, bullets, menu, bossalien, bossbullet,all_sprites)
            
        else:
            ship2.blitme()
            gf.update_screen(ai_settings, screen, stats, scoreboard, ship, ship2,aliens, bullets, menu, bossalien, bossbullet,all_sprites)

run_game()
