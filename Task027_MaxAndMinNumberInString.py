# 27. Строка содержит набор чисел. Показать большее и меньшее число
#     Символ-разделитель - пробел


def Get_min_value(input_data: str):
    temp_list = input_data.split()
    return min(temp_list)


def Get_max_value(input_data: str):
    temp_list = input_data.split()
    return max(temp_list)


data = '1 5 2 3 4 6 -1 7'
print(data)
min_value = Get_min_value(data)
max_value = Get_max_value(data)
print(f'min value = {min_value}, max value = {max_value}')
