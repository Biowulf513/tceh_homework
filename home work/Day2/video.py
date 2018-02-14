# -*- coding: utf-8 -*-
empty_tuple = tuple()
tuple1 = (1, )
tuple2 = (1, )
not_a_tuple = (1)
print (
    tuple1 == tuple2,
    tuple2 == not_a_tuple,
    type(not_a_tuple),
    not_a_tuple
)

print ( (1,2) == (1,2, ))

tuple1 = tuple1 + tuple2
print(tuple1)

tuple1 = (2, ) + tuple1 + (not_a_tuple, )
print(tuple1)

print(len(tuple1), len(tuple2), len(empty_tuple))
print(tuple2[0], tuple1[0:2], tuple1[:-1])

print('=================')


multi = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]
for i in multi:
    print(i)
    for element in i:
        print('element -', element)

s = {'one': 1, 'two': 2, '4': 'IV'}

print(s.items())

for key, value in s.items():
    print(key, value)
