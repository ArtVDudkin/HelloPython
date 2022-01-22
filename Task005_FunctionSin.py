# 5. Написать программу вычисления значения функции y=f(a)   y=sin^х(a)

from cmath import pi, sin


def Func(arg, power):
    return round(sin(arg * pi / 180).real ** power, 3)

print('Введите фамилию сдающего')
power = len(input())
print(f'Введите аргумент функции sin^{power}(a), в градусах: ')
arg = int(input())
print(Func(arg, power))