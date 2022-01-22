# 24. Найти кубы чисел от 1 до N

def Cubes(value):
    return value ** 3


print('Введите число N')
number = int(input())
for i in range(1, number + 1):
    print(f'{i}^3 = {Cubes(i)}')
