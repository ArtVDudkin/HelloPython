# 28. Подсчитать сумму цифр в числе

def SumDigits(value):
    value = abs(value)
    sum = 0
    while value != 0:
        sum += value % 10
        value //= 10
    return sum


print('Введите число A')
number = int(input())
print(SumDigits(number))
