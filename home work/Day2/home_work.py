# -*- coding: utf-8 -*-
print('\nQ1\n')
int_list = [2, 3, 7, 9, 4, 7, 5, 145]
sorted(int_list)
print(int_list)

# ======================================================
print('\nQ2\n')
five_array = {1:'1', 2:'2', 4:'4', 6:'6', 12:'12'}

for item in five_array:
    print(item, five_array[item])

print('\nVAR.2\n')

for key, value in five_array.items():
    print(f'{key} - {value}')

# ======================================================
print('\nQ3\n')
my_tuple = (10.2, 11.3, 52.1, 1.0, 23.234, 1.2, 21.3, 54, 12.01, 2.234)

print('max "{0}", min "{1}"'.format(max(my_tuple), min(my_tuple)))
# ======================================================
print('\nQ4\n')

my_words = ['Earth', 'Russia', 'Moscow']

print(' -> '.join(my_words))
# ======================================================
print('\nQ5\n')

trash_str = '/bin:/usr/bin:/usr/local/bin'
answer = trash_str.split(':')
print(answer)

# ======================================================
print('\nQ6\n')

for i in range(1,100):
    print(i, end=', ') if i % 7 == 0 else None

# ======================================================
print('\nQ7\n')

matrix = [[1, 2, 3],
          [11, 12, 13],
          [21, 22, 23],
          [31, 32, 33]]

for m in matrix:
    print(m)
    for i in m:
        print(i)

# ======================================================
print('\nQ8\n')

my_list = ['qwe', 123, True, None, {1:1}, (1,2,3,4)]

for obj in my_list:
    print(obj, my_list.index(obj))
# ======================================================
print('\nQ9\n')

gray_list = ['white', 'to-delete', 'green', 'red', 'to-delete', 'to-delete', 'to']
print(gray_list)

while 'to-delete' in gray_list:
    gray_list.remove('to-delete')

print(gray_list)

# ======================================================
print('\nQ10\n')

i = 10
while i:
    print(i)
    i -= 1