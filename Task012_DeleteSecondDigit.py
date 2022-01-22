# 12. Удалить вторую цифру трёхзначного числа

import numbers
import random


def DeleteSecondDigit(value):
    digit_1 = value // 100
    digit_3 = value % 10
    return digit_1 * 10 + digit_3


num = random.randint(100, 999)
print(num)
print(DeleteSecondDigit(num))
