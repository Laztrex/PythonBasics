# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.

import os
from time import gmtime, strftime


class NotNameError(Exception):
    def __init__(self):
        self.name = 'NotNameError'

    def __str__(self):
        return f'Поле имени содержит не только буквы: {self.name}'


class NotEmailError(Exception):
    def __init__(self):
        self.name = 'NotEmailError'

    def __str__(self):
        return f'поле емейл не содержит @ и .(точку): {self.name}'


class RegLog:

    def __init__(self, file):
        self.input_name_file = os.path.join(os.getcwd(), file)
        self.registrations_good_file = os.path.join(os.getcwd(), 'registrations_good.log')
        self.registrations_bad_file = os.path.join(os.getcwd(), 'registrations_bad.log')
        self.my_line = ''

    def read_it(self):
        with open(my_file.input_name_file, mode='r',
                  encoding='utf8') as log_file:
            for self.my_line in log_file.readlines():
                try:
                    my_file.check_log_file()
                except ValueError as exc:
                    my_file.write_file_error(name_error=exc)
                except (NotNameError, NotEmailError) as exc:
                    my_file.write_file_error(name_error=exc)

    def check_log_file(self):
        processed_string = self.my_line.split()
        if len(processed_string) == 3:
            if processed_string[0].isalpha():
                if '@' in processed_string[1] and '.' in processed_string[1]:
                    if int(processed_string[2]):
                        if 99 >= int(processed_string[2]) >= 10:
                            self.write_file_ok()
                        else:
                            raise ValueError('Age is out of range')
                else:
                    raise NotEmailError
            else:
                raise NotNameError
        else:
            raise ValueError

    def write_file_ok(self):
        with open(self.registrations_good_file, mode='a', encoding='utf8', ) as log_out_ok:
            log_out_ok.write(f'{self.my_line}')

    def write_file_error(self, name_error):
        with open(self.registrations_bad_file, mode='a', encoding='utf8') as log_out_bad:
            log_out_bad.write(f'{strftime("%Y-%m-%d", gmtime()):<{15}} В строке - {self.my_line.strip():{40}} '
                              f'ошибка - {type(name_error)}, ее параметры: {name_error}\n')


my_file = RegLog(file='others/registrations.txt')
my_file.read_it()
