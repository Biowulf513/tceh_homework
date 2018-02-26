# -*- coding: utf-8 -*-
# Поле, свойства: размер, количество кораблей

class map:


    def __init__(self):
        self.graphic_array = {'none':'_', 'hit':'▪', 'dead':'⨯', 'ship':'▩', 'shadow':'⬫' }
        self.long_x = 10
        self.long_y = 10
    # Создание списка с поляим карты
    def create(self):

        # генерация списка
        def map_generator():
            # перечень указателей столбцов
            letters = 'abcdefghij'
            yield list('  ' + letters)
            for i in range(self.long_y):
                array = list(self.graphic_array['none'] * self.long_y)
                if i < 9:
                    array.insert(0, ' ' + str(i + 1) + ' ')# Пофиксить + 1
                else:
                    array.insert(0, str(i + 1) + ' ')  # Пофиксить + 1
                yield array

        self.map_array = list(map_generator())

    def show(self):
        for line in self.map_array:
            print(' '.join(line))

    # def



mappi = map()
mappi.create()
mappi.show()
