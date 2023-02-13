# -*-coding:utf-8 -*-
# @Time : 2023/2/12 22:54
# @Author : wll
# @File : game_stats.py
# @SoftWare : Pycharm

import json


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息。"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 让游戏一开始处于非活动状态。
        self.game_active = False

        self.high_score = self.read_high_score()

    def reset_stats(self):
        """初始化随游戏进行可能变化的统计信息。"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        try:
            with open("game_high_score/high_score.json") as score_file:
                score = json.load(score_file)
                high_score = score
        except:
            with open("game_high_score/high_score.json", "w") as score_file:
                json.dump(0, score_file)
                return 0
        else:
            return high_score
