# 25. Найти сумму чисел от 1 до А

def SumForm1toA(value):
    sum = 0
    for i in range(1, value + 1):
        sum += i
    return sum


print('Введите число A')
number = int(input())
print(SumForm1toA(number))
