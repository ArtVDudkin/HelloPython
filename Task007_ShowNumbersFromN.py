# 7. Показать числа от -N до N

def ShowNumbers(value):
    res = ''
    for i in range(-value, value + 1):
        res += f'{i} '
    return res


print('Введите число N')
num = int(input())
print(ShowNumbers(num))