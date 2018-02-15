# -*- coding: utf-8 -*-
'''Игра крестики - нолики'''
# матрица игры
play_board = [['\\', '1', '2', '3'],
                  ['A','_','_','_'],
                  ['B','_','_','_'],
                  ['C','_','_','_']]
position_array = {'y': None, 'x': None}

# отрисовка матрицы
def print_game_table():
    for board_line in play_board:
        print(*board_line)

# функция ввода данных
def player_motion():
    position = input('Введите строку, столбик например (A, 2): ')
    position_array.update(check_position(position))

# Проверка введённых данных
def check_position(position):
    y_refactor_array = {'a': 1, 'b': 2, 'c': 3}
    if 2 > len(position.replace(' ','')) < 3 :
        return False
    else:
        return {'y':int(y_refactor_array[position[0]]), 'x':int(position[-1])}

# поиск введённой координаты на поле
def find_position():
    play_board[position_array["y"]][position_array["x"]] = '*'
    input(f'Поставить сюда?\n{print_game_table()}\n\nY/N ?: ')
    print_game_table()
# проверка координаты на заполненность

# изменение матрицы новыми данными
# ход бота
# проверка игры на завершение
# жизненный цикл программы

print_game_table()
player_motion()

# print(type(position_array['y']), type(position_array['x']))
find_position()