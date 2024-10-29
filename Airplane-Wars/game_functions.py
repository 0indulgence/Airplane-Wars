import sys
import pygame
from time import sleep
import time
import random
from ship import Ship
from bullet import Bullet
from bullet import BossBullet
from alien import Alien
from alien import BossAlien
from explosion import Explosion
from shop import Shop
from pygame.sprite import Group
global timer  # 定义全局变量

def check_events(ai_settings, screen, stats, sb, menu, ship,ship2, aliens, bullets,shop_button):
    # 按钮相应和鼠标事件
    for event in pygame.event.get():
        # 鼠标事件，获取点击位置
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_menu(ai_settings, screen, stats, sb, menu, ship,ship2,
                       aliens, bullets, mouse_x, mouse_y,shop_button)
        # 关闭窗口
        elif event.type == pygame.QUIT:
            save_and_quit(stats)
        # 键盘事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen,
                                 stats, sb, menu, ship,ship2, bullets, aliens)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship , ship2)


def check_keydown_events(event, ai_settings, screen, stats, sb, menu, ship,ship2, bullets, aliens):
    # 按下键盘
    # P切换“开始、暂停”
    if event.key == pygame.K_p:
        if not stats.game_active:
            start_new_game(ai_settings, screen, stats,
                           sb, ship, bullets, aliens)
        elif stats.game_active and not stats.game_paused:
            pause_game(stats, menu)
        elif stats.game_active and stats.game_paused:
            unpause_game(stats, menu)
    # ESC按键切换“暂停、不暂停”
    elif event.key == pygame.K_ESCAPE:
        if stats.game_paused:
            unpause_game(stats, menu)
        elif not stats.game_paused:
            pause_game(stats, menu)
    #C键切换攻击模式
    elif event.key == pygame.K_c:
        ship.shoot_type +=1

    # 右方向键
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # 上方向键
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    # 下方向键
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    # 左方向键
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # 右方向键
    elif event.key == pygame.K_4:
        ship2.moving_right = True
    # 上方向键
    elif event.key == pygame.K_2:
        ship2.moving_up = True
    # 下方向键
    elif event.key == pygame.K_3:
        ship2.moving_down = True
    # 左方向键
    elif event.key == pygame.K_1:
        ship2.moving_left = True
    
    # 在游戏时，按空格键
    elif event.key == pygame.K_SPACE and stats.game_active:
        #奇数 手动
        if ship.shoot_type%2 == 1:
            fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_LCTRL and stats.game_active:
        #奇数 手动
        if ship.shoot_type%2 == 1:
            fire_bullet(ai_settings, screen, ship2, bullets)
    #################################################################################################

    # Q键退出
    elif event.key == pygame.K_q:
        save_and_quit(stats)

def check_keyup_events(event, ship,ship2):
    # 响应松开按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    ###################################################################################     
    if event.key == pygame.K_4:
        ship2.moving_right = False
    elif event.key == pygame.K_1:
        ship2.moving_left = False
    elif event.key == pygame.K_2:
        ship2.moving_up = False
    elif event.key == pygame.K_3:
        ship2.moving_down = False
    # M键开商店
    elif event.key == pygame.K_m:
        # 创建商店实例
        shop = Shop()
        print (1)
        shop.draw(shop.screen)  # 进入商店
    #################################################################################
        

def check_menu(ai_settings, screen, stats, sb, menu, ship,ship2, aliens,
               bullets, mouse_x, mouse_y,shop_button):
    # 开始新游戏
    button_clicked = menu.play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_new_game(ai_settings, screen, stats, sb, ship,ship2, bullets, aliens)

    double_button_clicked = menu.double_play_button.rect.collidepoint(mouse_x, mouse_y)
    if double_button_clicked and not stats.game_active:
        menu.double_play_button.player_flag = 1
        print(4)
        start_new_game(ai_settings, screen, stats, sb, ship,ship, bullets, aliens)
    owner_button_clicked = menu.owner_button.rect.collidepoint(mouse_x, mouse_y)
    if owner_button_clicked and not stats.game_active:
        screen_width = 500
        screen_height = 700
        screen = pygame.display.set_mode((screen_width , screen_height ))  # 屏幕大小
        exit_button = pygame.Rect(10, 10, 50, 30)

                 # 绘制退出按钮
        exit_button.width = 65  # 修改按钮的宽度
        exit_button.height = 40  # 修改按钮的高度 
        filename = './resources/images/shop_quit.png'
        shop_quit = pygame.image.load(filename).convert()
        shop_quit = pygame.transform.scale(shop_quit, (exit_button.width, exit_button.height))
        screen.blit(shop_quit,( 10,  5))

        x_position = 125
        y_position = 100

        filename = './resources/images/Own.jpg'
        item_image = pygame.image.load(filename).convert()
        item_image = pygame.transform.scale(item_image, (100, 100))
        screen.blit(item_image, (x_position+75, y_position-50))

        filename = './resources/images/Information.png'
        item_image = pygame.image.load(filename).convert()
        item_image = pygame.transform.scale(item_image, (400, 400))
        screen.blit(item_image, (x_position-70 , y_position +100))
         # 刷新屏幕显示
        pygame.display.flip()
        flag = 0
        while flag != 328:
           screen.blit(ai_settings.background, (0, 0))  # 对齐的坐标

           for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                exit_button_clicked = exit_button.collidepoint(mouse_x, mouse_y)
                if exit_button_clicked and not stats.game_active:
                    flag = 328
                    break
            


    shop_button_clicked = shop_button.rect.collidepoint(mouse_x, mouse_y)
    if shop_button_clicked and not stats.game_active:
        # print(1)
        shop = Shop(ai_settings)
        while True:
            shop.screen.blit(ai_settings.background, (0, 0))  # 对齐的坐标
             # 按钮相应和鼠标事件
            for event in pygame.event.get():
                # 鼠标事件，获取点击位置
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                exit_button_clicked = shop.exit_button.collidepoint(mouse_x, mouse_y)
                if exit_button_clicked and not stats.game_active:
                    # print(2)
                    shop.flag = 328
                    break
                button_rect_clicked = shop.button_rect.collidepoint(mouse_x, mouse_y)
                if button_rect_clicked and not stats.game_active:

                    shop_buy_1(ship,bullets,ai_settings,screen,stats)
                    shop_buy_1(ship2,bullets,ai_settings,screen,stats)
                    

                button_rect_2_clicked = shop.button_rect_2.collidepoint(mouse_x, mouse_y)
                if button_rect_2_clicked and not stats.game_active:
                    shop_buy_2(ship,bullets,ai_settings,screen,stats)
                    shop_buy_2(ship2,bullets,ai_settings,screen,stats)
                    print("Clicked button 2!")
            if shop.flag == 328:
                break

def shop_buy_1(ship,bullets,ai_settings,screen,stats):
    #上传飞船图片并获取其外接矩阵
    ship.image = pygame.image.load('./resources/images/shop_buy_2.jpg')
    ship.image = pygame.transform.scale(ship.image, (80, 80))  # 设置图片大小
    ship.rect = ship.image.get_rect()
    ship.rect.x = -1000
    ship.rect.y = -1000
    ship.blitme()
    Bullet.flag += 1

def shop_buy_2(ship,bullets,ai_settings,screen,stats):
    #上传飞船图片并获取其外接矩阵
    ship.image = pygame.image.load('./resources/images/shop11.png')
    ship.image = pygame.transform.scale(ship.image, (80, 80))  # 设置图片大小
    ship.rect = ship.image.get_rect()
    ship.rect.x = -1000
    ship.rect.y = -1000
    ship.blitme()
    Bullet.flag2 += 1




def bossalien_fire_bullet(ai_settings, screen, bossalien, bossbullet, ship):
    # 创建一颗子弹
    BossBullet(ai_settings, screen, bossalien, ship)


def start_new_game(ai_settings, screen, stats, sb, ship, ship2,bullets, aliens):
    # 结束当前游戏并重新开始

    # 背景音乐
    play_bg_music(ai_settings)
    # 重置游戏属性
    ai_settings.initialize_dynamic_settings()
    stats.reset_stats(ai_settings)
    sb.prep_images()  # 重置记分牌图像
    stats.game_active = True
    stats.game_ended = False  # 重置游戏统计信息
    aliens.empty()
    bullets.empty()  # 清空外星人列表和子弹列表
    create_fleet(ai_settings, screen, ship, aliens,stats )
    ship.center_ship()  # 创建一群新的外星人，并让飞船居中
    ship2.center_ship()  # 创建一群新的外星人，并让飞船居中
    # 隐藏鼠标
    # pygame.mouse.set_visible(False)


def play_bg_music(ai_settings):
    pygame.mixer.music.set_volume(ai_settings.med_volume)
    bg_music = pygame.mixer.music.load('./resources/sound/bg.mp3')
    pygame.mixer.music.play(-1)


def pause_game(stats, menu):
    # 暂停游戏
    stats.game_paused = True
    pygame.mixer.music.pause()


def unpause_game(stats, menu):
    # 继续游戏
    stats.game_paused = False
    pygame.mixer.music.unpause()


def stop_bg_music():
    # 音乐停止
    pygame.mixer.music.stop()


def save_and_quit(stats):
    # 保存（最高分）并退出
    game_data = './resources/data/high_score.txt'

    with open(game_data, 'w') as f_object:
        hs = int(stats.high_score)
        f_object.write(str(hs))

    sys.exit()


def update_screen(ai_settings, screen, stats, sb, ship,ship2, aliens, bullets, menu, bossalien, bossbullet,all_sprites):
    # 更新屏幕图像，切换新屏幕
    screen.blit(ai_settings.background, (0, 0))  # 对齐的坐标
    ship.blitme()
    ship2.blitme()
    sb.show_score()

    # 重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    if stats.level in stats.bosslevel:
        # boss关
        bossalien.blitme()
        bossalien.draw_health_bar(screen)
        if stats.game_active and not stats.game_paused:
            bossbullet.draw_bullet()

        bossalien_fire_bullet(ai_settings, screen, bossalien, bossbullet, ship)

        check_bossbullet(ai_settings, screen, stats, sb, ship, aliens, bossalien, bullets, bossbullet)
        all_sprites.update()
        all_sprites.draw(screen)

    else:
        # 非boss关
        for alien in aliens.sprites():
            alien.blitme()
        # aliens.draw(screen)

        bossalien.health=500 #重置boss血量
        all_sprites.update()#绘制爆炸特效
        all_sprites.draw(screen)




    # 游戏未开始，绘制play按钮
    if not stats.game_active and not stats.game_paused and not stats.game_ended:
        menu.draw_menu(stats)
    if stats.game_paused and stats.game_active:
        menu.draw_menu(stats)
    if stats.game_ended:
        menu.draw_menu(stats)

    # 屏幕可见
    pygame.display.flip()#翻页函数


def create_alien(ai_settings, screen, aliens, alien_number, row_number,stats):
    # 绘制外星人，放在当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    #40+2*40*（13+2）
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number - 2 * alien.rect.height * (stats.level+2)
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens,stats):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)  # 第一个对象是用来计算相关数据的
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.width, alien.rect.height)
    #增加难度——小怪排数量：关卡数+2
    for row_number in range(stats.level+2):
        for alien_number in range(number_aliens_x):
            a = random.random()
            if a > 0.3:
                create_alien(ai_settings, screen, aliens, alien_number, row_number,stats)


def update_aliens(ai_settings, stats, sb, menu, screen, ship,ship2, aliens, bullets, bossalien, bossbullet,all_sprites):
    #小怪关
    if stats.level not in stats.bosslevel:
        # 检查是否有外星人位于屏幕边缘，并更新外星人舰队中所有外星人的位置
        check_fleet_edges(ai_settings, aliens)  # 检查外星人是否位于屏幕边缘并向下移动
        aliens.update()  # 左右移动
        time.sleep(0.01)

        # 检测外星人和飞船直接的碰撞
        if pygame.sprite.spritecollideany(ship, aliens):
            expl3 = Explosion(ship.rect.center)
            all_sprites.add(expl3)

            ship_hit(ai_settings,screen,stats, sb, ship, aliens, bullets, bossalien, bossbullet)

        if pygame.sprite.spritecollideany(ship2, aliens):
            expl3 = Explosion(ship2.rect.center)
            all_sprites.add(expl3)

            ship_hit(ai_settings,screen,stats, sb, ship2, aliens, bullets, bossalien, bossbullet)
    #boss关
    else:
        check_bossalien_edges(ai_settings, bossalien, bossbullet)
        bossalien.update()


def get_number_aliens_x(ai_settings, alien_width):
    # 计算每行可容纳外星人数量
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    # 计算屏幕能容纳多少行外星人
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    #print(number_rows)
    return number_rows


def check_fleet_edges(ai_settings, aliens):
    """有外星人得到边界时"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(alien)


def check_aliens_bottom(ai_settings, stats, sb, menu, screen, ship, aliens, bullets, bossalien, bossbullet):
    # 外星人到底部
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 处理（跟飞船碰撞一样）
            ship_hit(ai_settings,screen,  stats, sb,
                     ship, aliens, bullets, bossalien, bossbullet)
            break


def change_fleet_direction(alien):
    """将外星人下调，并改变方向"""
    alien.fleet_direction *= -1


def update_bullets(ai_settings, screen, stats, sb, menu, ship, aliens, bullets, bossalien, bossbullet,all_sprites):
    # 更新子弹位置，删除消失的子弹

    # 更新子弹位置
    bullets.update()

    if stats.level in stats.bosslevel:
        if stats.game_active:
            bossbullet.update(ship,bossbullet)

    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)



    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, bossalien, bossbullet,all_sprites)
    # 底部的外星人
    check_aliens_bottom(ai_settings, stats, sb, menu,
                        screen, ship, aliens, bullets, bossalien, bossbullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    fire_sfx = pygame.mixer.Sound('./resources/sound/shoot.wav')
    fire_sfx.set_volume(ai_settings.low_volume)

    # 如果还没有到达限制，就发射一颗子弹
    # 创建子弹，并加入库中
    if len(bullets) < ai_settings.bullets_allowed :
        new_bullet = Bullet(ai_settings, screen, ship)
        pygame.mixer.Sound.play(fire_sfx)
        bullets.add(new_bullet)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, bossalien, bossbullet,all_sprites):
    # 响应 打击到外星人
    # 删除子弹和外星人
    # 非boss关
    if stats.level not in stats.bosslevel:
        
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        for hit in collisions:
            expl = Explosion(hit.rect.center)  # 实例化爆炸对象，爆炸中心=敌人中心位置
            all_sprites.add(expl)

        
        """
            collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
            for bullet in bullets:
                for  bullet,aliens in collisions.items():
                    for alien in aliens:
                        alien.health -= 1
                        expl2 = Explosion(bullet.rect.center)
                        all_sprites.add(expl2)
                        bullets.remove(bullet)
                        if alien.health == 0:
                            expl = Explosion(alien.rect.center)  # 实例化爆炸对象，爆炸中心=敌人中心位置
                            all_sprites.add(expl)
                            aliens.remove(alien)
                    
        """
        if collisions:
            for bullet in collisions:
                for alien in collisions[bullet]:
                    stats.score += (alien.points *ai_settings.alien_score_multiplier)  # 杀死外星人增加分数
                    sb.prep_score()  # 显示得分
            check_high_scores(ai_settings, stats, sb)  # 检查最高得分并显示

        # 外星人被消灭光，创建新的外星人（开始下一关）
        if len(aliens) == 0:
            start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # boss关
    elif stats.level in stats.bosslevel:

        # 子弹击中BOSS外星人，BOSS外星人失去一定血量
        for bullet in bullets:
            if pygame.Rect.colliderect(bullet.rect, bossalien.rect):
                expl2 = Explosion(bullet.rect.center)
                all_sprites.add(expl2)
                bossalien.health -= 100
                bullets.remove(bullet)

        # 生命值为0时删除该BOSS
        if bossalien.health <= 0:
            # 提高等级，加分
            stats.level += 1
            sb.prep_level()
            stats.score += ai_settings.bossalien_points
            sb.prep_score()
            check_high_scores(ai_settings, stats, sb)

            create_fleet(ai_settings, screen, ship, aliens,stats)

        """BOSS发射子弹和船碰撞"""
        #print(bossbullet.rect,"!",ship.rect)
        if pygame.Rect.colliderect(bossbullet.rect, ship.rect):
            expl4 = Explosion(ship.rect.center)
            all_sprites.add(expl4)
            all_sprites.draw(screen)
            pygame.display.flip()
            ship_hit(ai_settings, screen, stats,sb, ship, aliens, bullets, bossalien, bossbullet)



# 下一关
def start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets):
    next_level_sfx = pygame.mixer.Sound('./resources/sound/next_level.wav')
    next_level_sfx.set_volume(ai_settings.med_volume)

    bullets.empty()
    ai_settings.increase_speed()
    stats.level += 1  # 提高等级
    sb.prep_level()
    pygame.mixer.Sound.play(next_level_sfx)
    create_fleet(ai_settings, screen, ship, aliens,stats)  # 新建外星舰队


def check_high_scores(ai_settings, stats, sb):
    # 检查是否有得分新高

    new_hs_sfx = pygame.mixer.Sound('./resources/sound/high_score.wav')
    new_hs_sfx.set_volume(ai_settings.med_volume)
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        if stats.high_score_achieved:
            pass
        else:
            pygame.mixer.Sound.play(new_hs_sfx)
            stats.high_score_achieved = True
        sb.prep_high_score()


def ship_hit(ai_settings, screen,stats, sb,  ship, aliens, bullets, bossalien, bossbullet):
    # 响应被外星人撞到的飞机

    ship_hit_sfx = pygame.mixer.Sound('./resources/sound/ship_hit.wav')
    game_over_sfx = pygame.mixer.Sound('./resources/sound/game_over.wav')
    game_over_sfx.set_volume(ai_settings.med_volume)
    ship_hit_sfx.set_volume(ai_settings.low_volume)
    # 音乐
    pygame.mixer.Sound.play(ship_hit_sfx)

    # 还没结束
    if stats.ships_left > 0:
        stats.ships_left -= 1  # 扣血
        sb.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并将飞船放到屏幕底部中央

        if stats.level not in stats.bosslevel:
            # 非boss关
            create_fleet(ai_settings, screen, ship, aliens,stats)
            ship.center_ship()
        else:
            ship.center_ship()
            bossbullet.reset_position(bossalien)


        sleep(0.5)
    # 三条命全没了
    else:
        stats.game_active = False
        stats.game_ended = True
        pygame.mouse.set_visible(True)
        stop_bg_music()
        pygame.mixer.Sound.play(game_over_sfx)
        """boss射击"""


def check_bossbullet(ai_settings, screen, stats, sb, ship, aliens, bossalien, bullets, bossbullet):
    """当子弹飞出屏幕底部时，重置BOSS子弹位置"""
    screen_rect = screen.get_rect()
    if bossbullet.y >= screen_rect.bottom:
        bossbullet.reset_position(bossalien)


def check_bossalien_edges(ai_settings, bossalien, bossbullet):
    """检查BOSS外星人是否碰到边缘"""
    if bossalien.check_edges():
        change_bossalien_direction(ai_settings, bossalien)


def change_bossalien_direction(ai_settings, bossalien):
    """改变BOSS外星人的方向"""

    ai_settings.bossalien_direction *= -1
