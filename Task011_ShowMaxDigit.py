# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

import random


def MaxDigit(value):
    digit_1 = value // 10
    digit_2 = value % 10
    if digit_1 > digit_2:
        return digit_1
    else:
        return digit_2


number = random.randint(10, 99)
print(number)
print(MaxDigit(number))
