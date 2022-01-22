# 27. Определить количество цифр в числе

def GetRazr(value):
    value = abs(value)
    razr = 0
    while value != 0:
        razr += 1
        value //= 10
    return razr


print('Введите число A')
number = int(input())
print(GetRazr(number))
