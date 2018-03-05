# -*- coding: utf-8 -*-
'''
+1.Дан класс:
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
# ===============================================================================================================

# Сделать менеджер контекста, который может переопределить значение lock на True внутри блока контекста.
from contextlib import contextmanager

# class Lock(object):
#     def __init__(self):
#         self.lock = False
#
# @contextmanager
# def locker(some_lock):
#     some_lock.lock = True
#     yield some_lock
#
# lock1 = Lock()
# with locker(lock1):
#     print(lock1.lock)
#
# print(lock1.lock)

# -2. Сделать менеджер контекста, который бы проглатывал все исключения вызванные в теле и писал их в консоль,
@contextmanager
def no_exceptions():
    message = None
    try:
        yield
    except Exception as E:
        message = ('log => {}'.format(E))
    finally:
        next(no_exceptions)

with no_exceptions():
    1 / 0  # => logs: ZeroDivisionError

with no_exceptions():
    print('Done!')  # => continues execution
    'qwe' * 'qwe'  # => logs: ZeroDivisionError

# with no_exceptions():


