# -*- coding: utf-8 -*-
'''Игра крестики - нолики'''
play_board = [[' ', '1', '2', '3'],
                  ['A','_','_','_'],
                  ['B','_','_','_'],
                  ['C','_','_','_']]
def game_view():
    for board_line in play_board:
        print(*board_line)

game_view()
def check_player_motion(x, y):
    pass

def player_motion():
    print('Куда ходим?')
    x = input('Строка: ')
    y = input('Столбец: ')
    return (x,y)

print(player_motion())