# -*- coding: utf-8 -*-
# Корабль, свойства: размер (длина), место на поле

# 1 корабль — ряд из 4 клеток («четырёхпалубный»)
# 2 корабля — ряд из 3 клеток («трёхпалубные»)
# 3 корабля — ряд из 2 клеток («двухпалубные»)
# 4 корабля — 1 клетка («однопалубные»)

class ship():
    def __init__(self):
        self.ships_array = [[4,1],[3,2],[2,3],[1,4]]

    def show(self):
        def ship_generator():
            for model in self.ships_array:
                while model[1]:
                    yield list('*' * model[0])
                    model[1] -= 1

        return ship_generator()