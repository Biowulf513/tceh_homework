# -*- coding: utf-8 -*-+
class Car:
    pass

c = Car()
print(c, type(c))

class Room:
    number = 'Room 1408'
    floor = 4

r = Room()
r1 = Room()

print(r.number, r1.number)
print(r.floor, r1.floor)

r.number = 1208
r.floor = '12 floor'

print(r.number, r1.number)
print(r.floor, r1.floor)

class Door:
    def open(self):
        print('self is', self)
        print('Door is open')
        self.opened = True

d = Door()
d.open()

class Terminal:
    def hello(self, name):
        print('self is', self )
        print('Hello,', name)

t = Terminal()
t.hello('Artme')

class Window:
    is_opened = False

    def open(self):
        self.is_opened = not self.is_opened
        print('Window is now', self.is_opened)

w = Window()
w1 = Window()

print('Статус окон', w.is_opened, w1.is_opened)
w.open()
print('Статус окон', w.is_opened, w1.is_opened)

