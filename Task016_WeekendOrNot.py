# 16. Дано число обозначающее день недели. Выяснить является номер дня недели выходным

import random


def IsWeekend(index):
    return index == 6 or index == 7


day_index = random.randint(1, 7)
print(day_index)
print(IsWeekend(day_index))
