from random import randint, sample

_holder = []
_bulls_cows = {'bulls': None, 'cows': None}


def make_number():
    global _holder
    _holder = []
    first_numeral = (randint(1, 9))
    _holder.append(first_numeral)
    a = sample(range(0, 10), 10)
    a.remove(first_numeral)
    _holder = _holder + sample(a, 3)
    return _holder


# -- генерирует повторяющиеся цифры --
# def make_number():
#     global _holder
#     _holder = []
#     for i in range(4):
#         if i == 0:
#             _holder.append(randint(1, 9))
#         else:
#             _holder.append(randint(0, 9))
#     return _holder


def check_number(input):
    bulls = []
    cows = []
    for i in range(4):
        if input[i] in _holder:
            if _holder[i] == input[i]:
                bulls.append(input[i])
                if input[i] in cows:
                    cows.remove(input[i])
            else:
                if input[i] not in bulls and input[i] not in cows:
                    cows.append(input[i])

    _bulls_cows['bulls'] = len(bulls)
    _bulls_cows['cows'] = len(cows)

    return _bulls_cows


def game_over():
    return _bulls_cows['bulls'] == 4
