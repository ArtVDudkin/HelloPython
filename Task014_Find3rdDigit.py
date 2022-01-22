# 14. Найти третью цифру числа или сообщить, что её нет

def CheckThirdDigit(value):
    if value > -100 and value < 100:
        return f'В числе {value} третья цифра отсутствует'
    else:
        return abs(value) // 100 % 10


print('Введите число')
num = int(input())
print(CheckThirdDigit(num))
