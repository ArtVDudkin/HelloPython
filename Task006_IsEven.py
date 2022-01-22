# 6. Выяснить является ли число чётным

def IsEven(value):
    return value % 2 == 0


print('Введите число')
num= int(input())
print(IsEven(num))