# 20. Определить, присутствует ли в заданном списке строк, некоторое число


def Find_number_in_string(input_data: list, search_num):
    res = False
    for e in input_data:
        if str(search_num) in e:
            res = True
    return res


data = ["йцу", "фыв", "ячс", "цук", "йцу123н", "йцу"]
search_number = 123
print(f'Результаты поиска {search_number} в {data}:')
res = Find_number_in_string(data, search_number)
print(res)
