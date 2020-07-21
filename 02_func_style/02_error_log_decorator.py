# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


# def log_errors(func):
#
#     def execute_first_function(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#         except Exception as exc:
#             with open(file='function_errors.log', mode='a', encoding='utf8') as log_out_bad:
#                 log_out_bad.write(f' В строке - {exc} \n')
#         else:
#             return result
#
#     return execute_first_function
#
#
# # Проверить работу на следующих функциях
# @log_errors
# def perky(param):
#     return param / 0
#
#
# @log_errors
# def check_line(line):
#     name, email, age = line.split(' ')
#     if not name.isalpha():
#         raise ValueError("it's not a name")
#     if '@' not in email or '.' not in email:
#         raise ValueError("it's not a email")
#     if not 10 <= int(age) <= 99:
#         raise ValueError('Age not in 10..99 range')
#
#
# lines = [
#     'Ярослав bxh@ya.ru 600',
#     'Земфира tslzp@mail.ru 52',
#     'Тролль nsocnzas.mail.ru 82',
#     'Джигурда wqxq@gmail.com 29',
#     'Земфира 86',
#     'Равшан wmsuuzsxi@mail.ru 35',
# ]
#
#
# for line in lines:
#     try:
#         check_line(line)
#     except Exception as exc:
#         print(f'Invalid format: {exc}')
# perky(param=42)


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass

def get_log_errors(file_name):
    def log_errors(func):
        def execute_first_function(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                with open(file=file_name, mode='a', encoding='utf8') as log_out_bad:
                    log_out_bad.write(f' В фунции {func.__name__} с параметром - {args, kwargs} '
                                      f'- ошибка типа {type(exc)} - {exc}\n')
            else:
                return result
        return execute_first_function
    return log_errors


# Проверить работу на следующих функциях
@get_log_errors(file_name='function_errors.log')
def perky(param):
    return param / 0


@get_log_errors(file_name='function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]

decorate_function_with_param = get_log_errors(file_name='function_errors.log')
check_line = decorate_function_with_param(check_line)

for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)

