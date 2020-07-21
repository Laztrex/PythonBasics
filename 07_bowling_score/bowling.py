# -*- coding: utf-8 -*-
import logging

log = logging.getLogger('bowling')


def configure_logging():
    log.setLevel(logging.INFO)
    file_log = logging.FileHandler('bowling.log', encoding='utf-8')
    file_log.setFormatter(logging.Formatter('\n %(asctime)s %(levelname)s %(message)s'))
    log.addHandler(file_log)


class LengthStringIncorrect(Exception):
    def __init__(self):
        self.name = 'LengthStringError'

    def __str__(self):
        return f'Неправильная информация о бросках. Должно быть четное количество, макс. - 20. ' \
               f'Обратитесь в help {self.name}'


class PinSizeError(Exception):
    def __init__(self):
        self.name = 'PinSizeError'

    def __str__(self):
        return f'Количество сбитых кеглей за 2 броска больше 10! Проверьте правильность введенных данных или ' \
               f'обратитесь в help {self.name}'


class SpareIncorrectError(Exception):
    def __init__(self):
        self.name = 'SpareIncorrectError'

    def __str__(self):
        return f'Ошибка в расположении очков "spare". Проверьте правильность введенных данных или ' \
               f'обратитесь в help {self.name}'


class MaxCountStrikeError(Exception):
    def __init__(self):
        self.name = 'MaxStrikeCountError'

    def __str__(self):
        return f'Превышено кол-во страйков на 10 фреймов. Проверьте правильность введенных данных или ' \
               f'обратитесь в help {self.name}'


class BowlingScoreCalc:

    def __init__(self):
        configure_logging()
        self.count_strikes = 0

    def get_score(self, game_result):
        try:
            result = self._calculation_scores(game_result)
            log.info(f'Количество очков для результатов {game_result} - {result}')
            return result
        except (TypeError, ValueError, LengthStringIncorrect,
                PinSizeError, SpareIncorrectError, MaxCountStrikeError) as exc:
            log.exception(f'Недопустимые символы в данных - {exc}')
            raise

    def _calculation_scores(self, scores):
        total_score = []
        new_scores = [''.join(i) for i in self._grouper(scores, 2)]
        for throw in new_scores:
            total_score += self._check_scores(throw)
        return sum(total_score) + self.count_strikes * 20

    def _grouper(self, input_data, n):
        input_data = self._count_strike(input_data.upper(), "X")
        if len(input_data) % 2 != 0 or len(input_data) > 20:
            raise LengthStringIncorrect
        args = [iter(input_data)] * n
        return zip(*args)

    def _count_strike(self, input_data, symbol):
        self.count_strikes = input_data.count(symbol)
        if self.count_strikes > 10:
            raise MaxCountStrikeError
        if self.count_strikes == 0:
            if "Х" in input_data:
                return self._count_strike(input_data, "Х")
            else:
                return input_data
        return input_data.replace(symbol, "")

    def _check_scores(self, data):
        for element_1, element_2 in data.split():
            if element_1 == "/":
                raise SpareIncorrectError
            elif element_2 == "/":
                return [15]
            elif data and "-" in data:
                return [int(i) for i in data if i.isnumeric()]
            else:
                sum_scores = int(element_1) + int(element_2)
                if sum_scores <= 10:
                    return [sum_scores]
                else:
                    raise PinSizeError
