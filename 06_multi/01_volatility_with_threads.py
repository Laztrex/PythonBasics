# -*- coding: utf-8 -*-

import csv
import os
import time
from collections import defaultdict
from collections import Counter
from termcolor import cprint
from time_lord import time_track
import queue
import threading


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
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
#


class Ticker(threading.Thread):

    def __init__(self, file_name, file_object, dict_total, null_list, lock1, lock2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scan_folder = os.path.join(os.getcwd(), file_name)
        self.file_object = file_object
        # TODO: у нас два пошаренных между тредами объекта, но один лок для них. А зачем блокировать соседний тред для второго объекта, когда мы пользуем первый?
        # TODO: Честно говоря, медитировал над вопросом, но так и не понял, на что он должен навести. Чтобы поток одновременно с первым не полез в общий котел?
        # TODO: Для каждого shared объекта использовать свой лок. Либо как-то уменьшить число локов.
        self.volatility_dict = dict_total
        self.volatility_list = null_list
        self.min_current = 0
        self.max_current = 0
        self.tracker_secid = ''
        self.dict_lock = lock1
        self.list_lock = lock2

    def run(self):
        try:
            self._worker()
        except Exception as exc:
            print(exc)

    def _worker(self):
        with open(os.path.join(self.scan_folder, self.file_object)) as file_obj:
            reader = csv.DictReader(file_obj)
            for line in reader:
                self.min_max_definition(line)
            self.volatility_calculation()

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
            with self.list_lock:  # TODO: А нужны ли здесь вообще локи? Операции же атомарные
                             # TODO: https://stackoverflow.com/questions/6319207/are-lists-thread-safe
                             # TODO: короче, если это не Queue то лучше все операции модификации делать под локом
                self.volatility_list.append(self.tracker_secid)
            cprint(f'\r{round(len(self.volatility_list) * 7.14)}%', end='', flush=True, color='blue')
        else:
            average = (self.max_current + self.min_current) / 2
            with self.dict_lock:
                self.volatility_dict[self.tracker_secid] = \
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


@time_track
def main(research_folder):
    volatility_folder = os.path.join(os.getcwd(), research_folder)
    volatility_dict = defaultdict(lambda: dict)
    null_volatity_list = []
    threads_active = []
    my_lock = threading.Lock()
    my_lock_too = threading.Lock()

    for filename in os.listdir(volatility_folder):
        ticker = Ticker(
            file_name=research_folder,
            file_object=filename,
            dict_total=volatility_dict,
            null_list=null_volatity_list,
            lock1=my_lock,
            lock2=my_lock_too
        )
        ticker.start()
        threads_active.append(ticker)

    for ticker in threads_active:
        ticker.join()

    print_results(volatility_dict, null_volatity_list)


if __name__ == '__main__':
    main(research_folder='trades')
# зачет!
