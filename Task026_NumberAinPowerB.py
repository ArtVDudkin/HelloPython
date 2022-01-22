# 26. Возведите число А в натуральную степень B используя цикл

def PowerAinB(value, power):
    res = 1
    for i in range(1, power + 1):
        res *= value
    return res


print('Введите число A')
number = int(input())
print('Введите степень')
power = int(input())
print(PowerAinB(number, power))
