# 11. Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д


def Sequence(value):
    sequence = (-3) ** value
    return sequence


def Fill_list(value):
    out_list = []
    for i in range(value):
        out_list.append(Sequence(i))
    return out_list


def Check_value(value):
    while not value.isnumeric():
        print(f'Введите целое число')
        value = input()
    res = int(value)
    return res


print('Введите целое число')
n = Check_value(input())

data_list = Fill_list(n)
print(data_list)
