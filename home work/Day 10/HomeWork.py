# -*- coding: utf-8 -*-
#Реализовать на Flask
from flask import Flask, json
# from json import dumps, loads

app = Flask(__name__)

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
#3. По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'
'''4. По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля. Необходимо валидировать email, что обязательно присутствует, валидировать пароли, что они минимум 6 символов в длину и совпадают. Возрващать пользователю json вида: 
 "status" - 0 или 1 (если ошибка валидации),
 "errors" - список ошибок, если они есть,
 или пустой список.
'''
#5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files. Файлы можно туда положить любые текстовые. А если такого нет - 404.

if __name__ == '__main__':
    app.run()