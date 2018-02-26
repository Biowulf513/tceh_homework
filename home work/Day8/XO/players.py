# -*- coding: utf-8 -*-
class Player:
    col_player = 0
    badge_variants = ['X', 'O']
    def __init__(self):
        self.name = input('Введите имя игрока: ')
        Player.badge(self)
        Player.col_player += 1

    def badge(self):
        if self.col_player == 0:
            print('Выбери чем будешь ходить')
            self.badge = Player.badge_variants.pop(int(input('0 : {}, 1 : {}: '.format(Player.badge_variants[0], Player.badge_variants[1]))))
        else:
            self.badge = Player.badge_variants[0]