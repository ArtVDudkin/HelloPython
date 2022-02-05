# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30

def Devider_of_5_and_10_or_15_but_not_30(value):
    return ( (value % 5 == 0) and (value % 10 == 0) or (value % 15 == 0) ) and (value % 30 != 0)


print('Введите число')
num = int(input())
print(Devider_of_5_and_10_or_15_but_not_30(num))
