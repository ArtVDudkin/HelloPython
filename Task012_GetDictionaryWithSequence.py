# 12. Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


def Sequence(value):
    sequence = 3*value + 1
    return sequence


def Fill_dictionary(value):
    out_dict = {}
    for i in range(1, value + 1):
        out_dict[i] = Sequence(i)
    return out_dict


print('Введите целое число')
n = int(input())
new_dict = Fill_dictionary(n)
print(new_dict)
