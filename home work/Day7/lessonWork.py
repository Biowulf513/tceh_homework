def action_decorator(func):
    def inner(text):
        print('Someone is going to', func.__name__)
        func(text)

    return inner


@action_decorator  # try to uncomment me
def shout(text):
    print(text.upper(), '!!!!')


@action_decorator
def whisper(text):
    print(text.lower(), '...')


@action_decorator
def say(something):
    something += '; was said.'
    print(something)


if __name__ == '__main__':
    # Basic functions:
    say('hi')
    whisper('Hello')
    say('i am here')


# def dec_action(func):
#     def modify(text):
#         print('good')
#         func(text)
#
#     return modify
#
# @dec_action
# def ok(message):
#     message += ' !!!'
#     print(message)
#
# ok('ok')