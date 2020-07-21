# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
from multiprocessing import Process, Pipe, cpu_count
import csv
import os
from collections import defaultdict
from collections import Counter
from termcolor import cprint
from time_lord import time_track


class Ticker(Process):

    def __init__(self, file_location, file_container, conn, my_dict, my_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scan_folder = file_location
        self.file_object = file_container
        self.min_current = 0
        self.max_current = 0
        self.tracker_secid = ''
        self.conn = conn
        self.total_dict, self.null_list = my_dict, my_list

    # def tree():
    #     return lambda: dict
    # ......
    # volatility_dict, null_volatility_list = defaultdict(tree), []

    def run(self):
        try:
            self._worker()
        except Exception as exc:
            print(exc)

    def _worker(self):
        for file in self.file_object:
            with open(os.path.join(self.scan_folder, file)) as file_obj:
                reader = csv.DictReader(file_obj)
                for line in reader:
                    self.min_max_definition(line)
                self.volatility_calculation()
        self.conn.send([self.total_dict, self.null_list])
        self.conn.close()

    def min_max_definition(self, line):
        price = float(line['PRICE'])
        if line['SECID'] != self.tracker_secid:
            self.max_current, self.min_current = 0, price
            self.tracker_secid = line['SECID']
        else:
            if price > self.max_current:
                self.max_current = price
                if self.max_current < self.min_current:
                    self.max_current, self.min_current = self.min_current, self.max_current
            elif price < self.min_current:
                self.min_current = price

    def volatility_calculation(self):
        if self.max_current == 0:
            self.null_list.append(self.tracker_secid)
        else:
            average = (self.max_current + self.min_current) / 2
            self.total_dict[self.tracker_secid] = \
                round(((self.max_current - self.min_current) / average) * 100, 2)


def print_results(dict_total_prints, null_list):
    cprint('\n \n | Максимальная волатильность |', color='magenta')
    for ticker, value in dict(Counter(dict_total_prints).most_common(3)).items():
        print(f'{"":^5} {ticker} - {value} %')
    cprint('\n | Минимальная волатильность |', color='cyan')
    for ticker, value in dict(Counter(dict_total_prints).most_common()[-3:]).items():
        print(f'{"":^5} {ticker} - {value} %')
    cprint('\n | Нулевая волатильность |', color='green')
    for ticker in sorted(null_list):
        print(ticker, end=', ')


def grouping_volatility(iterable, count):
    """ Группировка элементов последовательности по count элементов """
    return zip(*[iter(iterable)] * count)


def tree():
    return lambda: dict


@time_track
def main(research_folder):
    volatility_folder = os.path.join(os.getcwd(), research_folder)
    files_list = os.listdir(volatility_folder)
    my_tickers, pipes = [], []
    volatility_dict, null_volatility_list = defaultdict(tree), []  # но здесь достаточно и просто {}
    crushing_for_processes = len(files_list) // cpu_count()

    for files in grouping_volatility(files_list, crushing_for_processes):
        parent_conn, child_conn = Pipe()
        ticker = Ticker(
            file_location=volatility_folder,
            file_container=files,
            conn=child_conn,
            my_dict=volatility_dict,
            my_list=null_volatility_list
        )
        my_tickers.append(ticker)
        pipes.append(parent_conn)

    for research_file in my_tickers:
        research_file.start()
    for conn in pipes:
        dict_values, list_value = conn.recv()
        volatility_dict.update(dict_values.items())
        null_volatility_list += list_value
    for ticker in my_tickers:
        ticker.join()

    print_results(volatility_dict, null_volatility_list)


if __name__ == '__main__':
    main(research_folder='trades')

