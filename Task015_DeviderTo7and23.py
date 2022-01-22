# 15. Дано число. Проверить кратно ли оно 7 и 23

def DeviderOf7and23(value):
    return (value % 7 == 0) and (value % 23 == 0)


print('Введите число')
num = int(input())
print(DeviderOf7and23(num))
