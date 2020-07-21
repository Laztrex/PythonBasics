# -*- coding: utf-8 -*-
import os
from termcolor import cprint
from random import randint, randrange, sample


# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money_warehouse = 100
        self.food_in_fridge = 50
        self.mud = 0
        self.food_for_pet = 0

    def __str__(self):
        return 'В доме денег {}, еды в холодильнике для людей {}, еды для котов {}, ' \
               'загрязненность {}'.format(self.money_warehouse,
                                          self.food_in_fridge, self.food_for_pet,
                                          self.mud)


class Human:
    total_fur_coat = 0
    total_money = 0
    total_food = 0
    total_stroke_pet = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return 'У {} сытость {}, а счастья {}'.format(self.name, self.fullness, self.happiness)

    def act(self, home, name):
        if home.mud > 90:
            self.happiness -= 10
        if self.fullness < 0:
            cprint('{} умер :('.format(self.name), color='red')
            return False
        if self.happiness < 10:
            cprint('{} умер :('.format(self.name), color='red')
            return False
        return True

    def eat(self, home):
        if home.food_in_fridge > 0:
            cprint('{} поел(а)'.format(self.name), color='blue')
            current_food = randint(10, 30)
            self.fullness += current_food
            home.food_in_fridge -= current_food
            Human.total_food += current_food
        else:
            self.fullness -= 10
            cprint('{} еды нет'.format(self.name), color='red')
            return False

    def stroke_cat(self):
        self.fullness -= 10
        self.happiness += 5
        Human.total_stroke_pet += 1
        cprint('{} погладил кота'.format(self.name), color='yellow')


class Pet(House):
    DIE_FACTOR = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 0

        super().__init__()
        self.food_for_pet = 100

    def __str__(self):
        return 'У {} сытость {}'.format(self.name, self.fullness)

    def act(self, home):
        if self.fullness < 0:
            cprint('{} умер :('.format(self.name), color='red')
            Pet.DIE_FACTOR += 1
            return False
        return True

    def eat(self, home):
        if home.food_for_pet >= 10:
            current_food_for_pet = randint(5, 10)
            home.food_for_pet -= current_food_for_pet
            self.fullness += 2 * current_food_for_pet
            cprint('{} покушал {} единиц еды'.format(self.name, current_food_for_pet), color='cyan')
        else:
            self.fullness -= 10
            cprint('В доме нет еды для котов!', color='red')

    def sleep(self):
        self.fullness -= 10
        cprint('{} спит'.format(self.name), color='cyan')


class Husband(Human):

    def __init__(self, name):
        super().__init__(name=name)
        self.current_salary = 150

    def __str__(self):
        return super().__str__()

    def act(self, home, name):
        home.mud += 5
        if super().act(home, name):
            dice = randint(0, 9)
            if self.fullness <= 20:
                self.eat(home)
            elif home.money_warehouse < 50 or 0 <= dice < 4:
                self.work(home)
            elif dice == 4 or 10 < self.happiness < 20:
                self.gaming()
            elif dice == 5:
                self.stroke_cat()
            else:
                self.eat(home)

    def work(self, home):
        self.fullness -= 10
        home.money_warehouse += self.current_salary
        Human.total_money += self.current_salary
        cprint('{} сходил на работу'.format(self.name), color='white')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint('{} поиграл в WoT'.format(self.name), color='blue')


class Wife(Human):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self, home, name):
        if super().act(home, name):
            dice = randint(0, 11)
            if self.fullness <= 20:
                if not self.eat(home):
                    self.shopping(home)
            elif home.food_in_fridge <= 40:
                self.shopping(home)
            elif home.food_for_pet <= 30:
                self.shopping(home)
            elif home.mud >= 50 or 0 <= dice < 3:
                self.clean_house(home)
            elif 10 <= self.happiness < 40:
                if home.money_warehouse > 350:
                    self.buy_fur_coat(home)
                else:
                    self.stroke_cat()
            elif dice <= 3:
                self.shopping(home)
            elif name.happiness % 100 == 0:
                self.buy_fur_coat(home)
            elif 4 <= dice < 10:
                self.stroke_cat()
            else:
                self.eat(home)

    def shopping(self, home):
        self.fullness -= 10
        if home.money_warehouse <= 0:
            cprint('Нет денег!', color='red')
        else:
            if home.food_in_fridge < 100:
                current_shop_food = randrange(50, 70, 10)
            elif 100 < home.food_in_fridge < 800:
                current_shop_food = randrange(30, 50, 10)
            else:
                current_shop_food = 10

            if home.food_for_pet < 40:
                current_shop_food_for_cat = randint(10, 50)
            else:
                current_shop_food_for_cat = 10

            home.food_in_fridge += current_shop_food
            home.food_for_pet += current_shop_food_for_cat
            home.money_warehouse -= current_shop_food + current_shop_food_for_cat
            cprint('{} сходила в супермаркет'.format(self.name), color='green')

    def buy_fur_coat(self, home):
        if home.money_warehouse >= 350:
            self.fullness -= 10
            home.money_warehouse -= 350
            self.happiness += 60
            Human.total_fur_coat += 1
            cprint('{} купила шубу!'.format(self.name), color='green')
        else:
            self.fullness -= 10
            self.happiness -= 10
            cprint('{} денег на шубу нет'.format(self.name), color='red')

    def clean_house(self, home):
        self.fullness -= 10
        if home.mud >= 100:
            home.mud -= randint(90, 100)
            cprint('{} сделала капитальную уборку в доме'.format(self.name), color='cyan')
        else:
            home.mud -= randint(5, home.mud)
            cprint('{} решила немного прибраться в доме'.format(self.name), color='cyan')


# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat(Pet):

    def __init__(self, name):
        super().__init__(name=name)
        self.fullness = 30

    def __str__(self):
        return super().__str__()

    def act(self, home):
        if super().act(home):
            dice = randint(0, 6)
            if self.fullness < 30:
                self.eat(home)
            elif dice < 2:
                self.soil(home)
            elif 2 <= dice < 4:
                self.sleep()
            else:
                self.eat(home)

    def soil(self, home):
        self.fullness -= 10
        home.mud += 5
        cprint('{} дерёт обои'.format(self.name), color='red')


# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Human):

    def __init__(self, name):
        super().__init__(name=name)
        self.happiness = 100

    def __str__(self):
        return super().__str__()

    def act(self, home, name):
        if self.fullness <= 10:
            cprint('{} умер :('.format(self.name), color='red')
        dice = randint(0, 6)
        if self.fullness <= 20:
            self.eat(home)
        elif dice < 3:
            self.sleep()
        else:
            self.eat(home)

    def eat(self, home):
        if home.food_in_fridge > 0:
            current_food_child = randint(7, 10)
            self.fullness += current_food_child
            home.food_in_fridge -= current_food_child
            Human.total_food += current_food_child
            cprint('{} покушал'.format(self.name), color='blue')
        else:
            self.fullness -= 10
            cprint('{} еды нет'.format(self.name), color='red')

    def sleep(self):
        self.fullness -= 10
        cprint('{} спит'.format(self.name), color='white')


class Simulation:

    def __init__(self, money_terror, food_terror):
        self.money_terror = sample(range(366), money_terror)
        self.food_terror = sample(range(366), food_terror)

    def experiment(self, current_salary, names_cats):

        home = House()
        serge = Husband(name='Сережа')
        masha = Wife(name='Маша')
        cats = [Cat(name=cat) for cat in names_cats]
        kolya = Child(name='Коля')

        serge.current_salary = current_salary
        Pet.DIE_FACTOR = 0

        for day in range(366):

            if day in self.money_terror:
                home.money_warehouse = round(home.money_warehouse // 2)
                cprint(f'{"+":-<8}{"+":-^}{"+":->{20}}\n'
                       f'| {"Половина денег пропало!!!":>{20}} |\n'
                       f'{"+":-<8}{"+":-^}{"+":->{20}}', color='red')
            if day in self.food_terror:
                home.food_in_fridge = round(home.food_in_fridge // 2)
                cprint(f'{"+":-<8}{"+":-^}{"+":->{20}}\n'
                       f'| {"Половина еды пропало!!!":>{20}} |\n'
                       f'{"+":-<8}{"+":-^}{"+":->{20}}', color='red')

            cprint('================== День {} =================='.format(day), color='red')
            serge.act(home, serge)
            masha.act(home, masha)
            kolya.act(home, kolya)
            for cat in cats:
                cat.act(home)
            cprint(serge, color='grey')
            cprint(masha, color='grey')
            cprint(kolya, color='grey')
            for cat in cats:
                cprint(cat, color='grey')
            cprint(home, color='grey')

        cprint('Зарплата в этом году {}'.format(current_salary), color='red')
        cprint('Всего съедено еды в этом году {}'.format(Human.total_food), color='magenta')
        cprint('Всего заработано денег в этом году {}'.format(Human.total_money), color='magenta')
        cprint('Всего куплено шуб в этом году {}'.format(Human.total_fur_coat), color='magenta')
        cprint('Всего поглаживаний котов в этом году {}'.format(Human.total_stroke_pet), color='magenta')

        if Pet.DIE_FACTOR != 0:
            return False
        else:
            return True

    def write_result_experiment(self, alive_cats):
        try:
            if os.stat("out_simulation").st_size == 0:
                self._write_init()
        except FileNotFoundError:
            self._write_init()
            self._results(alive_cats)
        else:
            self._results(alive_cats)

    def _write_init(self):
        with open(file='out_simulation', mode='w', encoding='utf8') as file_out:
            file_out.write(
                f'| {"Исчезновение еды":^{10}} | {"Исчезновение денег":^{10}} | {"Зарплата":^{10}} | '
                f'{"Выживет котов":^{10}} |\n')

    def _results(self, alive_cats):
        with open(file='out_simulation', mode='a', encoding='utf8') as file_out:
            file_out.write(f'| {food_incidents:^{16}} | {money_incidents:^{18}} | {salary:^{10}} | '
                           f'{alive_cats:^{13}} | \n')


# влить в мастер все коммиты из ветки develop и разрешить все конфликты

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов


for food_incidents in range(6):
    for money_incidents in range(6):
        life = Simulation(money_incidents, food_incidents)
        for salary in range(50, 401, 50):
            current_cats_alive = []
            for _ in range(3):
                mur_mur_list = ['Мурзик', 'Зевс', ]
                while True:
                    max_cats = life.experiment(current_salary=salary, names_cats=mur_mur_list)
                    if not max_cats:
                        break
                    mur_mur_list.append('Кексик')
                    continue
                current_cats_alive.append(len(mur_mur_list) - 1)
            print(f'При зарплате {salary} максимально можно прокормить '
                  f'{sum(current_cats_alive) // len(current_cats_alive)} котов')
            life.write_result_experiment(alive_cats=sum(current_cats_alive) // len(current_cats_alive))

cprint('\033[1m' + 'Результаты эксперимента записаны в файл - out_simulation.txt', color='blue')

# зачет!
