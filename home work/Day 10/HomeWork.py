# -*- coding: utf-8 -*-
#Реализовать на Flask
from flask import Flask, json, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
# from json import dumps, loads

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)

#1. По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']

@app.route('/locales')
def local_lson():
    local = {"ru":
                {"id": 1,
                "fullname" : "Russia",
                "language": "Russian",
                "capital_of_country": "Moscow",
                },
            "en":
                {"id": 2,
                "fullname" : "United States",
                "language": "English",
                "capital_of_country": "Washington",
                },
            "it":
                {"id": 3,
                "fullname" : "Italy",
                "language": "Italian",
                "capital_of_country": "Rome",
                }
            }

    response = app.response_class(
        response=json.dumps(local, sort_keys=True, indent=4),
        status=200,
        mimetype='application/json'
    )

    return response

#2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму

@app.route('/sum/<int:first>/<int:second>')
def url_summ(first, second):
    return str(first + second)

#3. По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'
@app.route('/greet/<user_name>')
def hello(user_name):
    return 'Hello, {}'.format(user_name)

'''4. По адресу /form/user должен принимать 
 POST запрос с параментрами: email, пароль, подтверждение пароля. 
 
 Необходимо валидировать email, что обязательно присутствует, 
 валидировать пароли, что они минимум 6 символов в длину 
 и совпадают. Возрващать пользователю json вида: 
 "status" - 0 или 1 (если ошибка валидации),
 "errors" - список ошибок, если они есть, или пустой список.
'''
class ContactForm(FlaskForm):
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    password = PasswordField('New Password', [
        validators.Length(min=6),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

@app.route('/form/user', methods=['GET', 'POST'])
def post_user():
    if request.method == 'POST':
        state = [{'status': None}, {'errors': None}]
        status = [400, 200]
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            state[0]['status'] = 1

        else:
            state[0]['status'] = 0
            state[1]['errors'] = dict(form.errors)

        response = app.response_class(
            response=json.dumps(state, sort_keys=True, indent=4),
            status=status[state[0]['status']],
            mimetype='application/json'
        )

        return response

    else:
        return 'POST запрос с параментрами:\
        email, пароль, подтверждение пароля. '

#5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files. Файлы можно туда положить любые текстовые. А если такого нет - 404.

if __name__ == '__main__':
    app.run()