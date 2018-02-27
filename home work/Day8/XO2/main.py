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
+сообщение о победе
 обработка исключений
'''

class XO:
    move_counter = 0
    game_play = True
    win_result_list = [[[1,1],[1,2],[1,3],[]],
                       [[2,1],[2,2],[2,3],[]],
                       [[3,1],[3,2],[3,3],[]],
                       [[1,1],[2,1],[3,1],[]],
                       [[1,2],[2,2],[3,2],[]],
                       [[1,3],[2,3],[3,3],[]],
                       [[1,3],[2,2],[3,1],[]],
                       [[1,1],[2,2],[3,3],[]],
                       ]

    def __init__(self):
        self.board = Board()
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.players_list = list([self.player1, self.player2])

    # ход игрока
    def player_turn(self):
        self.board.show_board()
        self.active_player = self.players_list[XO.move_counter % 2]
        print('Ходит {player} ({sign})'
              .format(player = self.active_player.name, sign = self.active_player.sign ))

        position = self.check_turn(input('Введите позицию хода: '))
        if self.board.check_position(position):  # Проверка ячейки на занятость
            self.add_user_position(position)
            self.check_win_result(position)
            XO.move_counter += 1

    # Добавление символа на игровую доску
    def add_user_position(self, position):
        self.board.board_list[position[1]][position[0]] = self.active_player.sign

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
                if not len(result_list[-1]) or self.active_player.sign in result_list[-1]:
                    result_list[-1].append(self.active_player.sign)

                elif self.active_player.sign not in result_list[-1]:
                    XO.win_result_list.remove(result_list)

            if XO.move_counter >= 4:
                # Есть ли комбинация с 3мя метками
                if len(result_list[-1]) >= 3:
                    XO.game_play = False
                    self.winner_detected(True)
                    break

                # Ничья
                elif XO.move_counter >= 7:
                    XO.game_play = False
                    self.winner_detected(False)
                    break

    def winner_detected(self, win):
        decor = '=' * 20

        print('\n{}'.format(decor))
        self.board.show_board()

        if win:
            print('{decor}\nPlayer {player} winer\n{decor}'
              .format(decor = decor, player = self.active_player.name.upper()))
        else:
            print('{decor}\nGAME OVER (DEAD HEAD)\n{decor}'
                  .format(decor=decor, player=self.active_player.name.upper()))

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
        try:
            if self.board_list[position[1]][position[0]] != '_':
                print('Увы данная позиция не свободна')
                return False
            else:
                return True
        except (IndexError, TypeError):
            print('Значение не входит в допустимые рамки')

class Player:
    sign_list = ['X', 'O']
    def __init__(self, number):
        self.name = input('Введите имя игрока{}: '.format(number))
        self.sign = Player.sign_list.pop(0)

if __name__ == '__main__':
    game1 = XO()
    while game1.game_play:
        game1.player_turn()