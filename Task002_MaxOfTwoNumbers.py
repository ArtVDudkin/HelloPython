# 2. Даны два числа. Показать большее и меньшее число

def MaxOfTwo(value_1, value_2):
    if value_1 > value_2:
        return f'Большее число {value_1}, меньшее число {value_2}'
    elif value_1 == value_2:
        return 'Введенные числа равны'
    else:
        return f'Большее число {value_2}, меньшее число {value_1}'


print('Введите два числа')
num_1 = int(input())
num_2 = int(input())
print(MaxOfTwo(num_1, num_2))