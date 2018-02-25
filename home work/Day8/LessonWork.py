
# -*- coding: utf-8 -*-
# • Нужно написать генератор, который бы каждый раз
# возвращал новое случайное значение

def random_gen():
    import random
    while True:
        yield random.randrange(0,100)

print(1, next(random_gen()))

# • Нужно написать генератор, который бы работал как
# range()

def range_gen(start, finish):
    a = start
    while True:
        if a == finish:
            break
        yield a
        a = a+1

range_num = list(range_gen(100, 140))
print(2, range_num)

# • Нужно написать генератор, который бы работал как
# map()

def map_gen(func, array):
    i = 0
    while i != len(array):
        yield func(array[i])
        i += 1

my_func = lambda x: x*2
my_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
gen_answer = list(map_gen(my_func, my_list))
print(3, gen_answer)

# • Нужно написать генератор, который бы работал как
# enumerate()
def my_enumerate(array):
    i = 0
    while i < len(array):
        yield (i, array[1])
        i += 1

enumerate_array = (1,2,3,4,5)
print(4, list(my_enumerate(enumerate_array)))

# • Нужно написать генератор, который бы работал как zip()
def my_zip(array1, array2):
    i = 0
    while i < len(array1) and i < len(array2):
        yield (array1[i], array2[i])
        i += 1

zip_int = [1,2,3,4,5]
zip_letter = ['a', 'b', 'c']

print(5, list(my_zip(zip_int, zip_letter)))