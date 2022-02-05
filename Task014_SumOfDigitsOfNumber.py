# 14. Подсчитать сумму цифр в вещественном числе.

def Sum_of_digits(value):
    temp = str(value).replace('.','')
    num = abs(int(temp))
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10
    return sum


number = -1111.111111
print(Sum_of_digits(number))
