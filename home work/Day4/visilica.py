# -*- coding: utf-8 -*-
quest_list = ((5 ,'pop', 'bob', 'eye', 'fly', 'box'),
              (10, 'apple', 'price', 'print', 'money', 'honey'),
              (15, 'system', 'python', 'django', 'framework', 'pattern'))
def round_generation():
    import random
    level = int(input('Сложность?\n1-Easy\n2-Normal\n3-Hard\n'))
    if level not in [1, 2, 3]:
        print('Ты совсем слепой?\nПеред табой же все возможные варианты!!!')
        level = random.randint(1, 3)
        print(f'Будем считать что ты нажал {level}')

    level -= 1
    word = random.randint(1, 5)

    live = quest_list[level][0]
    word = quest_list[level][word]

    return {'word':word, 'live':live }

def hide_word(word):
    secret = '*' * len(word)
    return list(secret)

def game_over(array):
    if array['live'] <= 0 :
        percent = round((100 / int(len(array['word']))) * int(len(array['word'])-(array['secret'].count('*'))))
        print('===========\nУвы ты проиграл!')
        print('за {move} шагов ты отгадал {percent}%,\nно увы все твои жизни кончились.\nЗагаднное слово {word}'\
            .format(
                move = str(array['move']),
                percent = percent,
                word = array['word']
        ))
    else:
        print('\n===========\nКруто, у тебя ушло всего {daed_live} жизней'.format(daed_live=array['move']-len(list(array['word']))))
        print('Слово {}'.format(str(array['word']).upper()))

def check_variant(array, letter):
    if len(letter) > 1 or not letter.isalpha():
        print('Ты втираешь мне какую-то дичь, соберись!')
        return array
    elif letter in array['word']:
        array['player_letter'] += letter
        array['move'] += 1
        counter = 0
        for i in array['word']:
            if i == letter:
                array['secret'][counter] = i
            counter += 1
    else:
        array['player_letter'] += letter
        array['move'] += 1
        print('данного символа нет')
        array['live'] -= 1
    return array

def player_motion(array):
    # print(array)
    while True:
        print('\nСлово: '+''.join(array['secret']))
        print('У тебя {} попыток\n-----------'.format(array['live']))
        player_variant = input('Введите предпологаемую букву: ').lower()
        if player_variant in array['player_letter']:
            print('Ты уже вводил этот символ')
            continue
        array = check_variant(array, player_variant)
        if array['live'] <= 0 or '*' not in array['secret']:
            game_over(array)
            break
        # print(array)

def game_init():
    game_array = round_generation()
    game_array['secret'] = hide_word(game_array['word'])
    game_array['move'] = 0
    game_array['player_letter'] = []

    player_motion(game_array)

game_init()