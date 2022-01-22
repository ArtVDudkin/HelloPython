# 30. Показать кубы чисел, заканчивающихся на четную цифру

def Cubes(value):
    return value ** 3


print('Введите число N')
number = int(input())
for i in range(1, number + 1):
    if i % 10 % 2 == 0:
        print(f'{i}^3 = {Cubes(i)}')
