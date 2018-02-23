# -*- coding: utf-8 -*-
from functools import wraps
from textwrap import wrap


def decor(func):
    def wrap(text, letter):
        print(letter * 10)
        func(text)
        print(letter * 10)

    return wrap

@decor
def hello(value):
    print(value)

hello('testing', '|')