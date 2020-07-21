# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата


class LogAnalyser:

    def __init__(self, file_name):
        self.working_str = ''
        self.file_name = file_name
        self.counter_dict = {}

    def action(self):
        with open(self.file_name, mode='r', encoding='utf8') as log_file:
            for line in log_file.readlines():
                if line.rstrip().endswith(' NOK'):
                    self.sorted_as(line)
                    self.counter()
            self.write_file_out()

    def sorted_as(self, line):
        self.working_str = line[1:-16]

    def counter(self):
        if self.working_str in self.counter_dict:
            self.counter_dict[self.working_str] += 1
        else:
            self.counter_dict[self.working_str] = 1

    def write_file_out(self):
        with open('log_out.txt', mode='w', encoding='utf8', ) as log_out:
            for date, amount in self.counter_dict.items():
                log_out.write(f'[{date}] {amount}\n')


class GroupHour(LogAnalyser):

    def sorted_as(self, line):
        self.working_str = line[11:-19]

    def write_file_out(self):
        with open('log_out.txt', mode='a', encoding='utf8', ) as log_out:
            for date, amount in self.counter_dict.items():
                log_out.write(f'В{date} часов - {amount}\n')


class GroupMonth(LogAnalyser):

    def sorted_as(self, line):
        self.working_str = line[6:-25]

    def write_file_out(self):
        with open('log_out.txt', mode='a', encoding='utf8', ) as log_out:
            for date, amount in self.counter_dict.items():
                log_out.write(f'В {date} месяце - {amount}\n')


class GroupYear(LogAnalyser):

    def sorted_as(self, line):
        self.working_str = line[1:-28]

    def write_file_out(self):
        with open('log_out.txt', mode='a', encoding='utf8', ) as log_out:
            for date, amount in self.counter_dict.items():
                log_out.write(f'В {date} году - {amount}\n')


log_inspector = LogAnalyser(file_name='others/events.txt')
log_inspector.action()

log_inspector_hour = GroupHour(file_name='others/events.txt')
log_inspector_hour.action()

log_inspector_month = GroupMonth(file_name='others/events.txt')
log_inspector_month.action()

log_inspector_year = GroupYear(file_name='others/events.txt')
log_inspector_year.action()
