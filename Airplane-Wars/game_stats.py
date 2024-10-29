import os
from settings import Settings

# 记录游戏进程
class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False
        self.game_paused = False
        self.game_ended = False

        self.high_score = self.get_high_score()
        self.reset_stats(ai_settings)

    # 重置所有关卡
    def reset_stats(self,ai_settings):
        self.ships_left = self.ai_settings.ship_limit
        self.level = 1
        self.high_score_achieved = False
        self.score = 0
        ai_settings.alien_score_multiplier = 1.5

####################################################################################################################
        self.bosslevel=[3,5,12,16,20,24,28,32,36,40]#boss关
####################################################################################################################

    # 记录高分
    def get_high_score(self):
        highscore_file = './resources/data/high_score.txt'

        try:
            with open(highscore_file) as f_object:
                if os.stat(highscore_file).st_size > 0:   # 如果文件中有内容
                    high_score = f_object.read()
                    return int(high_score)

        except FileNotFoundError:
            high_score = 0
            return int(high_score)

        else:
            high_score = 0
            return int(high_score)
