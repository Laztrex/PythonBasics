# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n+1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик

class PrimeNumbers:

    def __init__(self, n, func_dict):
        self.i, self.n = 0, n
        self.functions = func_dict
        self.it_number = ''

    def __iter__(self):
        self.i = 0
        self.list = []
        return self

    def __next__(self):
        while self.i < self.n:
            self.i += 1
            if self.i > 1:
                for prime in self.list:
                    if self.i % prime == 0:
                        break
                else:
                    self.list.append(self.i)
                    self.check_functions()
                    if self.it_number:
                        return '{}- {}'.format(self.it_number, self.i)
        raise StopIteration()

    def check_functions(self):
        self.it_number = ''
        for name_function, function_work in self.functions.items():
            if function_work(self.i):
                self.it_number += name_function + ' | '


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик

def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


def happy_number(n):
    list_number = list(map(int, str(n)))
    if len(list_number) % 2 == 0:
        return sum(list_number[0:len(list_number) // 2]) == sum(list_number[len(list_number) // 2:])
    else:
        return sum(list_number[0:len(list_number) // 2]) == sum(list_number[len(list_number) // 2 + 1:])


def polyndrom_number(n):
    list_number = list(map(int, str(n)))
    return list_number == list_number[::-1]


def armstrong_number(n):
    list_number = list(map(int, str(n)))
    result = sum(x ** len(list_number) for x in list_number)
    return result == n


functions_filters = {'Счастливое число': happy_number,
                     'Палиндром': polyndrom_number,
                     'Число Армстронга': armstrong_number
                     }

prime_number_iterator = PrimeNumbers(n=10000, func_dict=functions_filters)
for number in prime_number_iterator:
    print(number)


for name_function, function_work in functions_filters.items():
    result = filter(function_work, prime_numbers_generator(10000))
    print(f'Функция отработала и выдала: Простое {name_function} - {list(result)}')

# зачет! 