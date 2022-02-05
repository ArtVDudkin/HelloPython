# 10. Найти расстояние между двумя точками пространства 2D/3D

from math import sqrt


def Distance(dot_1, dot_2):
    res = 0
    for i in range(len(dot_1)):
        res += (dot_2[i] - dot_1[i]) ** 2
    return round(sqrt(res), 2)


dot_A = []
dot_B = []
data_is_valid = False

while (not data_is_valid):
    print('Введите координаты точки A через пробел')
    dot_A = list(map(int, input().split()))
    print('Введите координаты точки B через пробел')
    dot_B = list(map(int, input().split()))
    if len(dot_A) == 0:
        data_is_valid = False
        print('Ошибка! Координаты точки А не заданы')
    elif len(dot_B) == 0:
        data_is_valid = False
        print('Ошибка! Координаты точки B не заданы')
    elif len(dot_A) != len(dot_B):
        data_is_valid = False
        print('Ошибка! Количество введенных координат точек А и B не совпадает')
    else:
        data_is_valid = True

print(Distance(dot_A, dot_B))
