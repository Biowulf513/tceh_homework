# -*- coding: utf-8 -*-
# def quest():
quest_array = {'Какой язык мы учим' : 'python',
               'Что светит в небе' : 'солнце',
               'Как зовут Маска' : 'илон',
               'Какой бренд машин производит Илон' : 'tesla',
               }

col_correct_anwer = 0

for i in quest_array:
    answer = input(f'{i}?\n')
    if answer.lower() == quest_array[i]:
        print('Ответ верен')
        col_correct_anwer += 1
    else:
        print('Ответ не верен, правильный ответ "{}"'.format(quest_array[i]))

print(f'Ты правильно ответил на {len(quest_array)} вопросов,\nиз них правильно ответил на {col_correct_anwer}')