# Задачи

'''
+ Реализовать две функции: 
+write_to_file(data)
+read_file_data().
Которые соотвественно: пишут данные в файл и читают данные из файла.
'''
def write_to_file(file_name):
    with open(file_name, mode = 'a') as f:
        f.write('\n' + input('Введите текст: '))

def read_file_data():
    with open('test.txt') as f:
        print(f.read())

# write_to_file('test.txt')
# read_file_data()

'''
+ Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
(сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
выводить в консоль все пары заголовки, сохранять полученный json в файл на диск
'''
import requests, json

def requests_site(url, file):
    responce = requests.get(url)
    json_text = json.loads(responce.content)
    for post in json_text:
        print('{dec}\n{mail}\n{text}\n{dec}'.format(dec = '*' * 20, mail = post['email'], text = post['body']))

    with open(file, mode='a') as f:
       f.write(json.dumps(json_text, sort_keys=True, indent=4))


# requests_site('https://jsonplaceholder.typicode.com/comments', 'json.txt')

'''
+ Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
Ответить себе на вопрос удобно ли так делать?
'''
def habra_parsing():
    import re
    site = requests.get('https://habrahabr.ru/')
    html = site.text

    return list(re.findall(r'<a href="(\S+)"', html))


print(habra_parsing())