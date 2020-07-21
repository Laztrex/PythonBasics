# -*- coding: utf-8 -*-

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.my_cat_name = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='green')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def play_playstation(self):
        cprint('{} играл в playstation целый день'.format(self.name), color='blue')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food < 15:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.bowl < 20:
            self.buy_food_cat()
        elif self.house.mud >= 100:
            self.clean_in_house()
        elif dice == 1:
            self.work()
        elif 2 <= dice < 4:
            self.eat()
        else:
            self.play_playstation()

    def get_a_cat(self, house):
        print('Подобрали кота')
        cprint('<<Привет, я {}. Где еда и лежанка?>>'.format(my_sweet_cat.name),
               color='green')
        my_sweet_cat.house = house
        self.my_cat_name = my_sweet_cat.name

    def buy_food_cat(self):
        cprint('{} купил еды коту'.format(self.name), color='magenta')
        self.house.bowl += 50
        self.house.money -= 50

    def clean_in_house(self):
        cprint('{} сделал уборку'.format(self.name), color='cyan')
        self.house.mud -= 100
        self.fullness -= 20


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.bowl = 0
        self.mud = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кошачей еды осталось {}, степень загрязнения дома {}'.format(
            self.food, self.money, self.bowl, self.mud)


class Cat:

    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = 0

    def sleep(self):
        cprint('{} спит и спит'.format(self.name), color='yellow')
        self.fullness -= 10

    def eat(self):
        if self.house.bowl >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.bowl -= 10
        else:
            cprint('{} МЯЯАУУ! Миска пуста'.format(self.name), color='red')

    def vandalism(self):
        cprint('{} ободрал обои!'.format(self.name), color='red')
        self.fullness -= 10
        self.house.mud += 5

    def act(self):
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(0, 9)
        if self.fullness < 10:
            self.eat()
        elif self.fullness > 60:
            self.sleep()
        elif dice < 5:
            self.eat()
        elif 5 < dice <= 7:
            self.vandalism()
        else:
            self.sleep()

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)


citizens = [
    Man(name='Вася'),
]

my_sweet_home = House()

name_cat = ['Барсик', 'Мурзик', 'Мо-Мо', 'Тимофей']
my_sweet_cat = None

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
        if len(name_cat) == 4 and day > 10 and my_sweet_home.money > 300:
            my_sweet_cat = Cat(name=name_cat.pop(randint(0, 3)))
            citisen.get_a_cat(house=my_sweet_home)
        elif my_sweet_cat is not None:
            my_sweet_cat.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
        if my_sweet_cat is not None:
            print(my_sweet_cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.


# citisen = Man(name='Вася')
# my_sweet_home = House()
#
# name_cat = [Cat(name='Барсик'), Cat(name='Мурзик'), Cat(name='Мо-Мо'), Cat(name='Тимофей')]
# citisen.go_to_the_house(house=my_sweet_home)
#
# for my_sweet_cat in name_cat:
#     citisen.get_a_cat(house=my_sweet_home)
#
# for day in range(1, 366):
#     print('================ день {} =================='.format(day))
#     for my_sweet_cat in name_cat:
#         my_sweet_cat.act()
#     citisen.act()
#     print('--- в конце дня ---')
#     for my_sweet_cat in name_cat:
#         print(my_sweet_cat)
#     print(citisen)
#     print(my_sweet_home)

