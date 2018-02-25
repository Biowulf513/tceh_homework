# -*- coding: utf-8 -*-
# Декораторы
def decorator(func):
    func.counter = 1

    def fake(value):
        print(func.__name__, 'Runs:', func.counter)
        func.counter += 1
        return 'fake:' + func(value)

    return fake

@decorator
def my_str(value):
    return str(value)

@decorator
def i_str(value):
    return str(value)

# print(my_str(123))
# print(my_str(2335))
# print(i_str([]))

# пример 2

import time

def timer(func):

    def sec(col):
        start = time.clock()
        result = func(col)
        print('time:{}'.format(time.clock() - start))
        return result

    return sec


@timer
def my_range(col):
    # time.sleep(5)
    return list(x for x in range(col))

my_range(1)

# пример 2