# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world!'

@app.route('/user/<username>')
def user(username):
    return f'Hello {username.upper()}!!!'

@app.route('/sum/<int1>&<int2>')
def web_sum(int1, int2):
    return '{0} + {1} = {2}'.format(int1, int2, int(int1) + int(int2))

@app.route('/string/<str1>&<str2>&<str3>')
def web_str(str1, str2=None, str3=None):
    return max([str1, str2, str3], key=len)

if __name__ == '__main__':
    app.run()