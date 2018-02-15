# -*- coding: utf-8 -*-

def random_error():
    import random
    error_list = [ValueError, TypeError, RuntimeError]
    error_var = random.randrange(0,3)
    raise error_list[error_var]

re = random_error
print(random_error)
re()
#
def list_sort(*args):
    for i in args:
        if isinstance(i,int):
            return sorted(args)
        else:
            raise TypeError('переданы аргументы классов отличных от int')


# print(list_sort(4,5,1,2,3,4,5,6))
# print(list_sort('a',5,1,2,3,4,5,6))

def array_refactor(array):

    print(array)

    clear_array = {}
    for k in array.keys():
        clear_array[str(k)] = array[k]
    return clear_array

bad_array = {1:1, 2:2, 3:3}
# print(array_refactor(bad_array))

def summ(*args):
    return sum(args)

# print(summ(1,2,3))