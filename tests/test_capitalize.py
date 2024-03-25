
from capitalize import capitalize

#if capitalize('hello') != 'Hello':
#    raise Exception('Функция работает неверно!')

#if capitalize('') != '':
#    raise Exception('Функция работает неверно!')


assert capitalize('') == ''
assert capitalize('hello') == 'Hello'

print('Все тесты пройдены!')


