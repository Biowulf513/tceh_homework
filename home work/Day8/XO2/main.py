# -*- coding: utf-8 -*-
'''
+ создаём поле
создаём игроков
    создание объекта игрок1
    создание объекта игрок2
ход игроков
    ввод позиции
            провека вводимого значения
        проверка не занята ли позиция
    
    установка знака на позицию
    проверка не выиграл ли игрок этим ходом
    ход другого игрока
    сообщение о победе
'''

class XO:
    def __init__(self):
        self.board = list(self.board_generator())

    # Генераор игровой доски
    def board_generator(self):
        x_name = (' ', 'A', 'B', 'C')
        y_name = ('1', '2', '3')
        yield x_name
        for y in y_name:
            line = list('_' * 3)
            line.insert(0, y)
            yield line
#
#
#
# game1 = XO()
# print(game1.board)