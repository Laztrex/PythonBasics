# -*- coding: utf-8 -*-

import os, time, shutil, zipfile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

path = 'others/icons.zip'
new_dir = 'icons_by_year'


class SortFiles:

    def __init__(self, scan_folder, target_folder):
        self.scan_dir = os.path.join(os.getcwd(), scan_folder)
        self.sorted_dir = os.path.join(os.getcwd(), target_folder)
        self.path_normalized = os.path.normpath(scan_folder)

    def go_scan(self):
        for dirpath, dirnames, filenames in os.walk(self.path_normalized):
            self.digging_in_guts(dirpath, filenames)

    def digging_in_guts(self, dirpath, filenames):
        for file in filenames:
            full_file_path = os.path.join(dirpath, file)
            secs = os.path.getmtime(full_file_path)
            file_time = time.gmtime(secs)
            self.copy_new_dir(full_file_path, new_path=self.new_path_generate(file_time=file_time))

    def copy_new_dir(self, full_file_path, new_path):
        shutil.copy2(full_file_path, new_path)

    def new_path_generate(self, file_time):
        new_path = os.path.join(self.sorted_dir, str(file_time[0]), str(file_time[1]))
        os.makedirs(new_path, exist_ok=True)
        return new_path


class SortZipFiles(SortFiles):

    def __init__(self, scan_folder, target_folder):
        super().__init__(scan_folder, target_folder)
        self.zfile = zipfile.ZipFile(self.scan_dir, 'r')

    def go_scan(self):

        for file in self.zfile.namelist():
            target_file = os.path.basename(file)
            if not target_file:
                continue
            source_file = self.zfile.open(file)
            file_time = self.zfile.getinfo(file).date_time
            target = open(os.path.join(self.new_path_generate(file_time), target_file), "wb")
            self.copy_new_dir(full_file_path=source_file, target=target)

    def copy_new_dir(self, full_file_path, target):
        shutil.copyfileobj(full_file_path, target)


scan_photo = SortFiles(scan_folder=path, target_folder=new_dir)
scan_photo.go_scan()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

scan_scan = SortZipFiles(scan_folder=path, target_folder=new_dir)
scan_scan.go_scan()

# TODO: Получился вариант через открытие файла и копирование объекта
#  Прошу помочь как разрешить тот вариант (__setattr__/__getattr__)?
# как вы сделали, это вполне ок
# зачет!


# class SortZipFiles(SortFiles):
#
#     def go_scan(self):
#         self.zfile = zipfile.ZipFile(self.scan_dir, 'r')
#         for zip_info in self.zfile.infolist():
#             if zip_info.filename[-1] == '/':
#                 continue
#             zip_info.filename = os.path.basename(zip_info.filename)  # TODO: :(
#             self.copy_new_dir(full_file_path=zip_info, new_path=self.new_path_generate(zip_info.date_time))
#
#     def copy_new_dir(self, full_file_path, new_path):
#         self.zfile.extract(full_file_path, new_path)
