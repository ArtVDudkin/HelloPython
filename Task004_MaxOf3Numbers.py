# 4. Найти максимальное из трех чисел

def MaxOfThree(value_1, value_2, value_3):
    max = value_1
    if value_2 > max:
        max = value_2
    if value_3 > max:
        max = value_3
    return max


print('Введите три числа')
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(MaxOfThree(num_1, num_2, num_3))