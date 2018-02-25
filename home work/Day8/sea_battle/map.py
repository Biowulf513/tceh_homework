# -*- coding: utf-8 -*-
# Поле, свойства: размер, количество кораблей

class map:
    def __init__(self):
        self.long_x = 10
        self.long_y = 10
    # Создание списка с поляим карты
    def create(self):

        # генерация списка
        def map_generator():
            # перечень указателей столбцов
            letters = 'abcdefghij'
            yield list('\\' + letters)
            for i in range(self.long_y):
                array = list('_' * self.long_y)
                array.insert(0, i + 1)# Пофиксить + 1
                yield array

        self.map_array = list(map_generator())

mappi = map()
mappi.create()
print(mappi.map_array)
