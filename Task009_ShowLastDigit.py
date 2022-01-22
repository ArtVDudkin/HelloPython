# 9. Показать последнюю цифру трёхзначного числа

import random


def LastDigit(value):
    return value % 10


num = random.randint(100, 999)
print(num)
print(LastDigit(num))
