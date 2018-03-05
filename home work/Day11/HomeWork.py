# -*- coding: utf-8 -*-
'''
-1.Дан класс:
class Lock(object):
    def __init__(self):
        self.lock = False

Сделать менеджер контекста, который может переопределить значение lock на True внутри блока контекста.
        
-2. Сделать менеджер контекста, который бы проглатывал все исключения вызванные в теле и писал их в консоль, 
пример использования:
with no_exceptions():
    1 / 0  # => logs: ZeroDivisionError

print('Done!')  # => continues execution

-3. Сделать менеджер контекста, который бы мог измерять время выполнения блока кода, пример использования:
with TimeIt() as t:
    some_long_function()

print('Execution time was:', t.time)
'''

