# 9. Показать вторую цифру трёхзначного числа

import random


def SecondDigit(value):
    return value // 10 % 10


num = random.randint(100, 999)
print(num)
print(SecondDigit(num))
