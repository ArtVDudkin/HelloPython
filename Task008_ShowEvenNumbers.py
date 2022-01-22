# 8. Показать четные числа от 1 до N

def IsEven(value):
    return value % 2 == 0


def ShowNumbers(value):
    res = ''
    for i in range(1, value + 1):
        if IsEven(i):
            res += f'{i} '
    return res


print('Введите число N')
num = int(input())
print(ShowNumbers(num))
