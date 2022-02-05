# 35. В файле находится N натуральных чисел, записанных через пробел. 
    # Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

with open('Task035.txt', 'r') as data:
    line = data.readline() + ' '            # искуственно добавляем пробел в конце строки для её дальнейшей обработки

numbers = []

while line != '':                           # пока строка не пустая
    space_pos = line.index(' ')             # ищем индекс первого пробела 
    numbers.append(int(line[:space_pos]))   # добавляем в список число, сконвертированное от начала строки до пробела
    line = line[space_pos + 1 :]            # отрезаем от строки начало вместе с пробелом

print(numbers)

def Find_lost_num(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i -1] + 1:
            lost_num = numbers[i -1] + 1
    return lost_num

print(Find_lost_num(numbers))