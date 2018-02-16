# -*- coding: utf-8 -*-
'''Игра крестики - нолики'''
# матрица игры
play_board = [['\\', '1', '2', '3'],
                  ['A','_','_','_'],
                  ['B','_','X','_'],
                  ['C','_','_','_']]
position_array = {'y': None, 'x': None}

def find_position_value(y = position_array['y'], x = position_array['x']):
    print(y, x)

# отрисовка матрицы
def print_game_table(array = play_board):
    for board_line in play_board:
        print(*board_line)

# функция ввода данных
def player_motion():
    # Ввод позиции
    while True:
        position = input('Введите строку, столбик например (A, 2): ')
        if check_position(position):
            break
        else:
            continue
    # Проверка позиции
    if check_position_value():
        find_position()
    else:
        player_motion()

# Проверка введённых данных
def check_position(position):
    y_refactor_array = {'a': 1, 'b': 2, 'c': 3}
    verified_position = {'y':None, 'x':None}
    position = position.replace(' ','')

    if 2 > len(position) or len(position) >= 3 :
        print('Неверное кол-во символов')
        return False
    point_position = {'y':position[0], 'x':position[-1]}

    if str(point_position['y']).lower() not in ('a', 'b', 'c'):
        print('Выбрана неверная строка')
        return False
    else:
        # print('Строка прошла проверку')
        verified_position['y'] = y_refactor_array[str(point_position['y']).lower()]

    if int(point_position['x']) not in (1, 2, 3):
        print('Выбран неверный столбец')
        return False
    else:
        # print('Столбец прошёл проверку')
        verified_position['x'] = int(point_position['x'])

    position_array.update(verified_position)
    # print(position_array)
    return True

# поиск введённой координаты на поле
def find_position():
    play_board[position_array['y']][position_array['x']] = '*'
    print_game_table()
    position_confirm = input('Поставить сюда?\n\nY/N ?: ')
    if position_confirm.lower() in ('y', 'yes', '+'):
        print('подтверждение получено')
        play_board[position_array['y']][position_array['x']] = 'X'
    elif position_confirm.lower() in ('n', 'no', '-'):
        print('отмена позиции')
        play_board[position_array['y']][position_array['x']] = '_'
    else:
        print('Введите правильное значение')
    print_game_table()

# проверка координаты на заполненность
def check_position_value():
    if play_board[position_array['y']][position_array['x']] == '_':
        print('Ячейка свободна')
        return True
    else:
        print('Ячейка занята')
        return False

# ход бота
# проверка игры на завершение
def check_end_game():
    win_condition = (((1, 1), (1, 2), (1, 3)),
                     ((2, 1), (2, 2), (2, 3)),
                     ((3, 1), (3, 2), (3, 3)),
                     ((1, 1), (2, 1), (3, 1)),
                     ((1, 2), (2, 2), (3, 2)),
                     ((1, 3), (2, 3), (3, 3)),
                     ((1, 1), (2, 2), (3, 3)),
                     ((1, 3), (2, 2), (3, 1)),
                    )
    for position_list in win_condition:
        i = 0
        for position in position_list:
            check_position_value()
            print(position[0], position[1])

# жизненный цикл программы
def init_game():
    print_game_table()
    while True:
        player_motion()
        print('----')
        find_position_value()

init_game()
# print(type(position_array['y']), type(position_array['x']))
# find_position()