# 29. Написать программу вычисления произведения чисел от 1 до N (это же факториал!)

def ProdFrom1toN(value):
    res = 1
    for i in range(1, value + 1):
        res *= i
    return res


print('Введите число A')
number = int(input())
print(ProdFrom1toN(number))
