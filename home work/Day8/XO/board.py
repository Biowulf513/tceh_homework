# -*- coding: utf-8 -*-

class Board(object):
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

    def show_board(self):
        for line in self.board:
            print(' '.join(line))

    def positions_in_board(self):

        self.show_board()


# a = Board()
# a.show_board()
# a.position_in_board(1,1)