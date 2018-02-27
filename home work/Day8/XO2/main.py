# -*- coding: utf-8 -*-
'''
+ создаём поле
+ создаём игроков
    + создание объекта игрок1
    + создание объекта игрок2
+ отображение поля
+ход игроков
    +ввод позиции
        +провека вводимого значения
        +преобразование буквенных значений в числовые
        +проверка не занята ли позиция
    
    +установка знака на позицию
    +добавление символа в список победных комбинаций
    +проверка всех комбинаций с данной позицией
    +если комбинация чиста или в ней уже есть метка игрока: записать на позицию в комбинации символ игрока
    +если в комбинации есть метка другого игрока удалить комбинацию из списка
    
    +ход другого игрока
сообщение о победе
'''

class XO:
    move_counter = 0
    finish = False
    win_result_list = [[[1, 1], [1, 2], [1, 3]],
                       [[2, 1], [2, 2], [2, 3]],
                       [[3, 1], [3, 2], [3, 3]],
                       [[1, 1], [2, 1], [3, 1]],
                       [[1, 2], [2, 2], [3, 2]],
                       [[1, 3], [2, 3], [3, 3]],
                       [[1, 1], [2, 2], [3, 3]],
                       [[1, 3], [2, 2], [3, 1]],
                       ]

    def __init__(self):
        self.board = Board()
        self.player1 = Player()
        self.player2 = Player()
        self.players_list = list([self.player1, self.player2])

    # ход игрока
    def player_turn(self):
        # while True:
        self.board.show_board()
        self.active_player = self.players_list[XO.move_counter % 2]
        print('Ходит {}'.format(self.active_player.name))

        position = self.check_turn(input('Введите позицию хода: '))
        if self.board.check_position(position):  # Проверка ячейки на занятость
            self.add_user_position(position)
            self.check_win_result(position)
            XO.move_counter += 1
        #     break
        # else:
        #     continue

    # Добавление символа на игровую доску
    def add_user_position(self, position):
        self.board.board_list[position[0]][position[1]] = self.active_player.sign
        self.board.show_board()

    # провека вводимого значения
    # преобразование буквенных значений в числовые
    def check_turn(self, position):
        x_position_dict = {'a':1, 'b':2, 'c':3}
        try:
            correct_position = []
            correct_position.insert(0, x_position_dict[position[0].lower()])
            correct_position.insert(1, int(position[-1]))
        except KeyError as E:
            print('Ты ввёл неверное значение столбика, что за {} ?'.format(E))
        except ValueError as E:
            print('Ты ввёл неверное строчки, что за {} ?'.format(E.args))
        else:
            return correct_position

    def check_win_result(self, position):

        for result_list in XO.win_result_list:
            if position in result_list:
                # если комбинация помечена соперником удаляем её и больше не проверяем
                if len(result_list) > 3 and result_list[-1] != self.active_player.sign:
                    XO.win_result_list.remove(result_list)
                else:
                    result_list.append(self.active_player.sign)
                    if len(result_list) >= 6:
                        self.winner_detected()
                        break

        # print(1, XO.win_result_list)

    def winner_detected(self):
        print('winner {}'.format(self.active_player.name))



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
        if self.board_list[position[0]][position[1]] != '_':
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
        if game1.finish == True:
            game1.winner_detected()
            break