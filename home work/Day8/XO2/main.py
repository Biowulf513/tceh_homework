# -*- coding: utf-8 -*-
'''
+ создаём поле
+ создаём игроков
    + создание объекта игрок1
    + создание объекта игрок2
+ отображение поля
ход игроков
    +ввод позиции
        +провека вводимого значения
        +преобразование буквенных значений в числовые
        +проверка не занята ли позиция
    
    +установка знака на позицию
        проверка не выиграл ли игрок этим ходом
    +ход другого игрока
сообщение о победе
'''

class XO:
    move_counter = 0
    def __init__(self):
        self.board = Board()
        self.player1 = Player()
        self.player2 = Player()
        self.players_list = list([self.player1, self.player2])

    # ход игрока
    def player_turn(self):
        while True:
            self.board.show_board()
            self.active_player = self.players_list[XO.move_counter % 2]
            print('Ходит {}'.format(self.active_player.name))
            position = self.check_turn(input('Введите позицию хода: '))
            if self.board.check_position(position):  # Проверка ячейки на занятость
                self.add_user_position(position)
                XO.move_counter += 1
                break
            else:
                continue

    # Добавление символа на игровую доску
    def add_user_position(self, position):
        self.board.board_list[position['x']][position['y']] = self.active_player.sign
        self.board.show_board()

    # провека вводимого значения
    # преобразование буквенных значений в числовые
    def check_turn(self, position):
        x_position_dict = {'a':1, 'b':2, 'c':3}
        try:
            correct_position = {}
            correct_position.update({'x':x_position_dict[position[0].lower()]})
            correct_position.update(dict( y = int(position[-1])))
        except KeyError as E:
            print('Ты ввёл неверное значение столбика, что за {} ?'.format(E))
        except ValueError as E:
            print('Ты ввёл неверное строчки, что за {} ?'.format(E.args))
        else:
            return correct_position

class Board:
    def __init__(self):
        self.board_list = list(self.board_generator())

    # Генераор игровой доски
    def board_generator(self):
        x_name = (' ', 'A', 'B', 'C')
        y_name = ('1', '2', '3')
        yield x_name
        for y in y_name:
            line = list('_' * 3)
            line.insert(0, y)
            yield line

    # Отображение игровой доски
    def show_board(self):
        for line in self.board_list:
            print(' '.join(line))

    # Проверка ячейки на занятость
    def check_position(self, position):
        if self.board_list[position['x']][position['y']] != '_':
            print('Увы данная позиция не свободна')
            return False
        else:
            return True

class Player:
    sign_list = ['X', 'O']
    def __init__(self):
        self.name = input('Введите имя игрока: ')
        self.sign = Player.sign_list.pop(0)

if __name__ == '__main__':
    game1 = XO()
    while True:
        game1.player_turn()