# -*- coding: utf-8 -*-
def decorator(func):
    def wrap():
        print('----------')
        print('{} in decorator1'.format(func.__name__))
        print(func())
        print('----------')

    return wrap

'''
*ЗАДАЧИ НА ДЕКОРАТОРЫ

+ Написать декоратор, который отменяет выполнение любой декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!
+ Реализовать декоратор, который измеряет скорость выполнения функций.
+ Реализовать декоратор, который будет считать, сколько раз выполнялась функция
+ Реализовать декоторатор, который будет логгировать процесс выполнения функции: создан декоратор, начато выполнение функции, закончено выполнение функции
+ Реализовать декоратор, который будет перехватывать все исключения в функции. Если они случились, нужно просто писать в консоль сообщение об ошибке
'''
# + Написать декоратор, который отменяет выполнение любой декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!
def decorator1(func):
    def wrap():
        raise Exception('function {} is canceled!'.format(func.__name__))

    return wrap

# + Реализовать декоратор, который измеряет скорость выполнения функций.
def decorator2(func):
    def wrap():
        import datetime, time
        start = datetime.datetime.now().microsecond
        print(func())
        # time.sleep(3)
        print('==========\nruntime = {run_time}.msec\n----------'.format(run_time=(datetime.datetime.now().microsecond - start)))

    return wrap

# + Реализовать декоратор, который будет считать, сколько раз выполнялась функция
def decorator3(func):
    run_list = []

    def wrap():
        func_name = str(func.__name__)
        run_list.append(func_name)
        func_col = run_list.count(func_name)
        print(func())
        print('это {} эапуск {}'.format(func_col, func_name))

    return wrap()

# + Реализовать декоторатор, который будет логгировать процесс выполнения функции:
#  создан декоратор, начато выполнение функции, закончено выполнение функции
def decorator4(func):
    def wrap():
        log_messages = ('создан декоратор', 'начато выполнение функции', 'закончено выполнение функции')
        print('==============================\n{}'.format(log_messages[0]))
        print(log_messages[1], func.__name__)
        print(func())
        print('{}\n=============================='.format(log_messages[2]))
    return wrap()

# + Реализовать декоратор, который будет перехватывать все исключения в функции.
# Если они случились, нужно просто писать в консоль сообщение об ошибке
def decorator5(func):
    def wrap():
        try:
            func()
        except Exception as error:
            print('Выпала ошибка', error)

    return wrap()


@decorator5
def test():
    message = 5/'yuiyui'
    if len(message) > 5:
        raise ValueError('ValueError:')

    return message








'''
*ЗАДАЧИ НА MAP/FILTER/REDUCE (И LAMBDA, ЕСЛИ НУЖНО)

- При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
- При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
- При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки
- При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']


*CЛОЖНОЕ ДОМАШНЕЕ ЗАДАНИЕ

**Технические требования:
- реализация игры морской бой друг против друга (играют два человека) по стандартным правилам https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D1%81%D0%BA%D0%BE%D0%B9_%D0%B1%D0%BE%D0%B9_(%D0%B8%D0%B3%D1%80%D0%B0)
- Остальные материалы в pdf-файле

**Усложненная версия игры:
- Реализовать возможность выбора с кем играем: человек или компьютер
- Реализовать для компьютера несколько стратегий игры (то есть уровней сложности)


*ТЕОРИЯ
**Менеджеры контекста
- Python with Context Managers: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
- contextlib: https://docs.python.org/3/library/contextlib.html и https://pymotw.com/2/contextlib/

**Декораторы
- Декораторы: http://thecodeship.com/patterns/guide-to-python-function-decorators/
- functools.wraps: https://docs.python.org/2/library/functools.html
- staticmethod vs classmethod: http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
- Декораторы с аргументами: http://scottlobdell.me/2015/04/decorators-arguments-python/

**Генераторы
- Генераторы: https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
- Зачем использовать генераторы? http://stackoverflow.com/questions/102535/what-can-you-use-python-generator-functions-for
- Как работает yield? https://habrahabr.ru/post/132554/
- Что такое yield from? http://old.pynsk.ru/posts/2015/Sep/21/sintaksis-python-yield-from/#.WfW6u9NJaRs

**Функциональные возможности
- lambdas: http://www.secnetix.de/olli/Python/lambda_functions.hawk
- Что такое late-binding: http://quickinsights.io/python/python-closures-and-late-binding/
- Замыкания: http://www.shutupandship.com/2012/01/python-closures-explained.html

**Другое
- Дата и время: https://pythonworld.ru/moduli/modul-datetime.html
- Списковые выражения: http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
'''