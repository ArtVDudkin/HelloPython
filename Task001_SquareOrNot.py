# 1. По двум заданным числам проверять является ли первое квадратом второго

def IsSquare(value_1, value_2):
    if value_1 == value_2 ** 2:
        return True
    else: 
        return False

print('Введите первое число')
number_1 = int(input())
print('Введите второе число')
number_2 = int(input())
print(IsSquare(number_1, number_2))