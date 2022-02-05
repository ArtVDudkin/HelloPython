# 6. Дано число, обозначающее день недели. Вывести его название и указать является ли он выходным.

import random


def Dayweek(index):
    days = ['Понедельник', 'Вторник', 'Среда',
            'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return days[index - 1]


def IsWeekend(index):
    return index == 6 or index == 7

day_index = random.randint(1, 7)
print(day_index)
print(Dayweek(day_index))
print(IsWeekend(day_index))
