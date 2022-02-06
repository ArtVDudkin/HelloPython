# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой


print('Введите исходную строку')
input_data = input()
print('Введите строку для поиска в исходной строке')
seek_value = input()

res = input_data.count(seek_value)
print(res)
