# -*- coding: utf-8 -*-
#
# *ЗАДАЧА 1:
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person), который позволяет
# добавить другого человека в список знакомых. И метод is_known(person), который возвращает знакомы ли два человека

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.know_humans = []

    def know(self, person):
        if person in self.know_humans:
            print('У {user} уже есть друг {person} !'.format(user = self.name, person = person.name))
        else:
            self.know_humans.append(person)

    def is_know(self, person):
        answer_array = {True : 'знакомы', False : 'не знакомы'}
        print('{my_person} и {other_person} {answer}!'.format(my_person = self.name, other_person = person.name, answer = answer_array[person in self.know_humans]))

user1 = Person(22, 'Alex')
user2 = Person(23, 'Anet')

user1.is_know(user2)
user1.know(user2)
user1.is_know(user2)

# *ЗАДАЧА 2:
# Есть класс, который выводит информацию в консоль: Printer, у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

class Printer:
    def log(self, *values):
        if type(self).__name__ == 'Printer':
            print(' '.join(values))
        else:
            return ' '.join(values)

class FormattedPrinter(Printer):
    def log(self, *values):
        print('*{}*'.format(super().log(*values)))

test = Printer()
test.log('i', 'am', 'the', 'law')

test1 = FormattedPrinter()
test1.log('i', 'am', 'the', 'law', 'arrr')



# *ЗАДАЧА 3:
# Написать класс Animal и Human,сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

class Animal:
    def __init__(self, type):
        self.type = type

class Human:
    weakness = ['хищник', 'ядовитый', 'агрессивный']

    def is_dangerous(self, animal):
        if animal.type.lower() in self.weakness:
            print('эта фигня опастна для меня')
        else:
            print('яб взял его домой, он совсем не опасен')
# Bob = Human()
#
# wolf = Animal('Хищник')
# dog = Animal('Домашний')
# cat = Animal('Домашний')
# snake = Animal('Ядовитый')
# bear = Animal('Агрессивный')
#
# animals = [wolf ,dog, cat, snake, bear]
#
# dir(Animal)
#
# for animal in animals:
#     Bob.is_dangerous(animal)



