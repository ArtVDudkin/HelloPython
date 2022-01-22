# 17. По двум заданным числам проверять является ли одно квадратом другого


def IsSquare(value_1, value_2):
    return value_1 == value_2 ** 2 or value_2 == value_1 ** 2


print('Введите два числа')
num_1 = int(input())
num_2 = int(input())
print(IsSquare(num_1, num_2))
