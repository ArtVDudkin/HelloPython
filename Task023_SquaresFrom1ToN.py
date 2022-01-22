# 23. Показать таблицу квадратов чисел от 1 до N

def Square(value):
    return value ** 2


print('Введите число N')
number = int(input())
for i in range(1, number + 1):
    print(f'{i}^2 = {Square(i)}')
