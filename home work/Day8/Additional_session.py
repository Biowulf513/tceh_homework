# -*- coding: utf-8 -*-
def decorator(func):
    func.counter = 1

    def fake(value):
        print('Runs:', func.counter)
        func.counter += 1
        return 'fake:' + func(value)

    return fake

@decorator
def my_str(value):
    return str(value)

@decorator
def i_str(value):
    return str(value)

print(my_str(123))
print(i_str([]))