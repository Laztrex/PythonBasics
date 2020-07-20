import unittest
from bowling import BowlingScoreCalc, LengthStringIncorrect, PinSizeError, SpareIncorrectError, MaxCountStrikeError
from unittest.mock import Mock
from termcolor import cprint


class GlobalScoreTest(unittest.TestCase):
    VALUES_FOR_TEST_NORMAL = ["X4/34", "4/X34", "34X4/", "4/34X"]
    VALUES_FOR_TEST_INCORRECT_SYMBOL = ['XX4\34', 'X4@74', 'X4X&34', '!#^%^)']
    VALUES_TEST_UNICODE = ["Х4/34", "4/Х34", "34Х4/", "4/34Х"]
    VALUES_TEST_INCORRECT_PINS = ["385511", "X99XXX", "766719", "XX-157"]
    VALUES_TEST_MAX_COUNT_STRIKES = ["X" * 12, "X" * 20, "X" * 16]
    VALUES_TEST_EVEN_PINS = ["11234", "9-518", "XX19-X", "4/X144"]
    VALUES_TEST_SPARE = ["////", "/453", "/X523", "/2/2"]
    VALUES_TEST_EMPTY = ["------", "--", "-3", "3-", "03"]

    def setUp(self):
        self.bowling_test = BowlingScoreCalc()
        cprint(f'Вызван {self.shortDescription()}', flush=True, color='cyan')

    def tearDown(self):
        cprint(f'Результаты теста записаны в bowling.log. \n', flush=True, color='grey')

    def test_normal(self):
        """Тест при нормальных условиях"""
        for value in self.VALUES_FOR_TEST_NORMAL:
            test_score = self.bowling_test.get_score(value)
            self.assertEqual(test_score, 42)

    def test_incorrect_symbol(self):
        """Тест при некорректных символах"""
        for value in self.VALUES_FOR_TEST_INCORRECT_SYMBOL:
            with self.assertRaises(ValueError):
                self.bowling_test.get_score(value)

    def test_unicode(self):
        """Тест при Х - кириллицой"""
        for value in self.VALUES_TEST_UNICODE:
            test_score = self.bowling_test.get_score(value)
            self.assertEqual(test_score, 42)

    def test_incorrect_bowling_pins(self):
        """Тест на корректное кол-во сбитых кеглей"""
        for value in self.VALUES_TEST_INCORRECT_PINS:
            with self.assertRaises(PinSizeError):
                self.bowling_test.get_score(value)

    def test_max_count_strikes(self):
        """Тест на корректное кол-во страйков"""
        for value in self.VALUES_TEST_MAX_COUNT_STRIKES:
            with self.assertRaises(MaxCountStrikeError):
                self.bowling_test.get_score(value)

    def test_even_number_pins(self):
        """Тест на четное кол-во сбитых кеглей (введенных данных)"""
        for value in self.VALUES_TEST_EVEN_PINS:
            with self.assertRaises(LengthStringIncorrect):
                self.bowling_test.get_score(value)

    def test_incorrect_spare(self):
        for value in self.VALUES_TEST_SPARE:
            with self.assertRaises(SpareIncorrectError):
                self.bowling_test.get_score(value)

    def test_empty(self):
        """Тест на пустые значения"""
        test_result_empty = [0, 0, 3, 3, 3]
        for i, value in enumerate(self.VALUES_TEST_EMPTY):
            test_score = self.bowling_test.get_score(value)
            self.assertEqual(test_score, test_result_empty[i])


class HiddenFunctionsTest(unittest.TestCase):
    """
    Тесты для внутренних функций модуля bowling.py
    test_grouper: тестирует метод _grouper для сортировки значений [n * 2]
    test_count_strike: тестирует метод _count_strike для подсчета страйков
    test_check_scores: тестирует метод _check_scores для интерпретации значений
    """
    TEST_STRIKES_RESULTS_FOR_2 = ["522/", "44", "43", "11", "4/5/"]
    TEST_STRIKES_RESULTS_FOR_3 = ["522/44", "114/5/", "4//777"]
    TEST_STRIKES_RESULTS_FOR_5 = ["522/44114/", "5/4//77711", "4/5/-1"]
    TEST_STRIKES = ["X522/", "x44", "Х43", "х11"]
    TEST_CHECK_SYMBOLS = ['6/', '25', '2-', ]

    def setUp(self):
        self.bowling_functions_test = BowlingScoreCalc()
        cprint(f'Вызван {self.shortDescription()}', flush=True, color='cyan')

    def test_grouper(self):
        """Тест на группировку
        тестировать без страйков - без X
        """
        result_groupes_2 = [["52", "2/"], ["44"], ["43"], ["11"], ["4/", "5/"]]
        result_groupes_3 = [["522", "/44"], ["114", "/5/"], ["4//", "777"]]
        result_groupes_5 = [["522/4", "4114/"], ["5/4//", "77711"], ["4/5/-"]]

        for i, score_grouping in enumerate(self.TEST_STRIKES_RESULTS_FOR_2):
            self.assertEqual(self._expression_for_grouper_test(score_grouping, 2), result_groupes_2[i])
        for i, score_grouping in enumerate(self.TEST_STRIKES_RESULTS_FOR_3):
            self.assertEqual(self._expression_for_grouper_test(score_grouping, 3), result_groupes_3[i])
        for i, score_grouping in enumerate(self.TEST_STRIKES_RESULTS_FOR_5):
            self.assertEqual(self._expression_for_grouper_test(score_grouping, 5), result_groupes_5[i])

    def _expression_for_grouper_test(self, mock, number_grouping):
        count_strikes = Mock(return_value=mock)
        self.bowling_functions_test._count_strike = Mock()
        self.bowling_functions_test._count_strike = count_strikes
        return [''.join(i) for i in self.bowling_functions_test._grouper(mock, number_grouping)]

    def test_count_strike(self):
        """Тест на подсчет страйков"""
        for i, with_strike_symbol in enumerate(self.TEST_STRIKES):
            a = self.bowling_functions_test._count_strike(with_strike_symbol.upper(), "X")
            self.assertEqual(a, self.TEST_STRIKES_RESULTS_FOR_2[i])

    def test_check_scores(self):
        """Тест на поиск spare и промахов"""
        test_results = [[15], [7], [2]]
        for i, symbol in enumerate(self.TEST_CHECK_SYMBOLS):
            a = self.bowling_functions_test._check_scores(data=symbol)
            self.assertEqual(a, test_results[i])


if __name__ == '__main__':
    unittest.main()
