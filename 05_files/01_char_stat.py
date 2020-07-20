# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile

from termcolor import cprint


class StatisticLetter:
    total_letters = 0

    def __init__(self, file_name):
        self.letter_list = []
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename, path='others/')
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file.readlines():
                for letter in line:
                    if letter.isalpha():
                        if letter in self.stat:
                            self.stat[letter] += 1
                        else:
                            self.stat[letter] = 1
            StatisticLetter.total_letters = sum(self.stat.values())
            self.sorted_stat()

    def sorted_stat(self):
        for char, count in self.stat.items():
            self.letter_list.append([count, char])
        self.letter_list.sort(reverse=True)
        self.print_amount_sort()

    def _it_stranger_letter(self, char, count):
        if char == 'ё':
            self.letter_list.append(['ее', count])
        elif char == 'Ё':
            self.letter_list.append(['ЕЕ', count])
        else:
            self.letter_list.append([char, count])

    def print_amount_sort(self):
        print(f'{"+":-<8}{"+":-^}{"+":->{len(str(StatisticLetter.total_letters)) + 3}}\n'
              f'| {"буква":^} | {"частота":>{len(str(StatisticLetter.total_letters))}} |\n'
              f'{"+":-<8}{"+":-^}{"+":->{len(str(StatisticLetter.total_letters)) + 3}}')
        for couple in self.letter_list:
            print(f'| {couple[1]:^5} | {couple[0]:>{len(str(StatisticLetter.total_letters))}} |')
        print(f'{"+":-<8}{"+":-^}{"+":->{len(str(StatisticLetter.total_letters)) + 3}}\n'
              f'| {"итого":^} | {StatisticLetter.total_letters:>{len(str(StatisticLetter.total_letters))}} |\n'
              f'{"+":-<8}{"+":-^}{"+":->{len(str(StatisticLetter.total_letters)) + 3}}')

    def printed_alphabet_sort(self):
        print(f'{"+":-<8}{"+":-^}{"+":->{len(str(StatisticLetter.total_letters)) + 3}}\n'
              f'| {"буква":^} | {"частота":>{len(str(StatisticLetter.total_letters))}} |\n'
              f'{"+":-<8}{"+":-^}{"+":->{len(str(StatisticLetter.total_letters)) + 3}}')
        for couple in self.letter_list:
            if couple[0] == 'ее':
                couple[0] = 'ё'
                print(f'| {couple[0]:^5} | {couple[1]:>{len(str(StatisticLetter.total_letters))}} |')
            elif couple[0] == 'ЕЕ':
                couple[0] = 'Ё'
                print(f'| {couple[0]:^5} | {couple[1]:>{len(str(StatisticLetter.total_letters))}} |')
            else:
                print(f'| {couple[0]:^5} | {couple[1]:>{len(str(StatisticLetter.total_letters))}} |')
        print(f'{"+":-<8}{"+":-^}{"+":->{len(str(StatisticLetter.total_letters)) + 3}}\n'
              f'| {"итого":^} | {StatisticLetter.total_letters:>{len(str(StatisticLetter.total_letters))}} |\n'
              f'{"+":-<8}{"+":-^}{"+":->{len(str(StatisticLetter.total_letters)) + 3}}')


class SortAscending(StatisticLetter):

    def sorted_stat(self):
        self.letter_list = []
        for char, count in self.stat.items():
            self.letter_list.append([count, char])
        self.letter_list.sort()
        self.print_amount_sort()


class SortAlphabetAscending(StatisticLetter):

    def sorted_stat(self):
        self.letter_list = []
        for char, count in self.stat.items():
            self._it_stranger_letter(char, count)
        self.letter_list.sort()
        self.printed_alphabet_sort()


class SortAlphabetDescending(StatisticLetter):
    def sorted_stat(self):
        self.letter_list = []
        for char, count in self.stat.items():
            self._it_stranger_letter(char, count)
        self.letter_list.sort(reverse=True)
        self.printed_alphabet_sort()


def start_stat(file):

    char_stat = StatisticLetter(file_name=file)
    char_stat.collect()

# После выполнения первого этапа нужно сделать упорядочивание статистики

    cprint('\n - по частоте по возрастанию', color='blue')
    chat_stat_sorted_ascending = SortAscending(file_name=file)
    chat_stat_sorted_ascending.collect()

    cprint('\n - по алфавиту по возрастанию', color='blue')
    stat_alphabet_ascending = SortAlphabetAscending(file_name=file)
    stat_alphabet_ascending.collect()

    cprint('\n - по алфавиту по убыванию', color='blue')
    stat_alphabet_descending = SortAlphabetDescending(file_name=file)
    stat_alphabet_descending.collect()

# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# зачет!


if __name__ == '__main__':
    start_stat(file='others/voyna-i-mir.txt.zip')
