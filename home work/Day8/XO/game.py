# -*- coding: utf-8 -*-
from abc import *
class Game:
    from random import randrange
    player_queue = randrange(2,3)
    def __init__(self, board, players):
        self.board = board
        self.players = players

    def check_position(self, position):
        if 2 > len(position) or len(position) > 3:
            raise ValueError('Не верное значение')
        else:
            return True


    def player_motion(self):
        player = self.players[Game.player_queue%2]
        print('ходит игрок {}'.format(player.name))
        while True:
            position = (input('Куда ходишь:'))
            print(position)
            if self.check_position(position):
                player.new_motion(list([position[0], position[-1]]))
                print(2, player.name, 3, player.motion_array)
                break
            else:
                continue

        Game.player_queue += 1


