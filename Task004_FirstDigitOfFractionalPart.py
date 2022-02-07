# 4. Показать первую цифру дробной части числа

import random


def First_digit_after_point(value):
    return int(abs(value) * 100 // 10 % 10)


number = random.uniform(-100, 100)
print(number)
res = First_digit_after_point(number)
print(res)
