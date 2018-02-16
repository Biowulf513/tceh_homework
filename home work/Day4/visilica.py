# -*- coding: utf-8 -*-
quest_list = ((5 ,'pop', 'bob', 'eye', 'fly', 'box'),
              (10, 'apple', 'price', 'print', 'money', 'honey'),
              (15, 'system', 'python', 'django', 'framework', 'pattern'))

def print_game(level, word):
    print(quest_list[level][word])

def start_game():
    import random
    level = input('Сложность?\n1-Easy\n2-Normal\n3-Hard\n')
    word = random.randint(1, 5)

    print_game()

# print_game(1, 3)
start_game()