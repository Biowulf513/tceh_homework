# -*- coding: utf-8 -*-
'''
Практическое задание
• Администратор задает seed для модуля рандом через
переменную окружения FLASK_RANDOM_SEED
• Flask при старте сервера - устанавливает seed для
random, генерирует случайное число для угадывания
+ Пользователь по GET запросу на адрес / получает
сообщение: "Число загадано"
+ Пользователь по POST запросе на адрес /guess
получает один из следующих результатов: ">", "<", "="
+ Если число угадано - загадываем новое число
'''
# ========================================================
from flask import Flask, request
from flask_wtf import Form
from wtforms import IntegerField, validators

app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'This key must be secret!',
    WTF_CSRF_ENABLED = False,
)

secret_int = [5, 10, 15, 20]

# Пользователь по GET запросу на адрес / получает
# сообщение: "Число загадано"
@app.route('/')
def main_page():
    return 'Число загадано !!!'

# Пользователь по POST запросе на адрес /guess
# получает один из следующих результатов: ">", "<", "="

class ContactForm(Form):
    number = IntegerField('int', [validators.Required()])

@app.route('/guess', methods=['POST'])
def guess():

    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            guess_array = {'user_var': request.form['number'],
                           'symbol' : None,
                           'message' : None}

            if int(guess_array['user_var']) > secret_int[0]:
                guess_array['symbol'] = '>'
            elif int(guess_array['user_var']) < secret_int[0]:
                guess_array['symbol'] = '<'
            else:
                secret_int.pop(0) # удаляем текущее значение секретного значения, тем самым меняем его на следующее
                guess_array['message'] = '"New secret value"'
                guess_array['symbol'] = '='

            return '{} {} secret {}'.format(guess_array['user_var'], guess_array['symbol'], guess_array['message'] if guess_array['message'] != None else ' ')

        else:
            return 'Bad Value (only int)!!!'

if __name__ == '__main__':
    app.run()
