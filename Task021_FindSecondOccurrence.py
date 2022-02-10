# 21. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#     Примеры
#     список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#     список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#     список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#     список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#     список: [], ищем: "123", ответ: -1


def Find_second_occurrence(input_data: list, search_text, occur):
    if search_text == '':
        return input_data
    else:
        second_occur = -1
        count = 0
        for i in range(len(input_data)):
            if input_data[i] == search_text:
                count += 1
                if count == occur:
                    second_occur = i

        return second_occur


occur = 2                                           # ищем второе вхождение элемента в списке

data = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
search_text = "qwe"
print(f'Результаты поиска {search_text} в {data}:')
res = Find_second_occurrence(data, search_text, occur)
print(res)                                          # res = 3

data = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
search_text = "йцу"
print(f'Результаты поиска {search_text} в {data}:')
res = Find_second_occurrence(data, search_text, occur)
print(res)                                          # res = 5

data = ["йцу", "фыв", "ячс", "цук", "йцукен"]
search_text = "йцу"
print(f'Результаты поиска {search_text} в {data}:')
res = Find_second_occurrence(data, search_text, occur)
print(res)                                          # res = -1

data = ["123", "234", 123, "567"]
search_text = "123"
print(f'Результаты поиска {search_text} в {data}:')
res = Find_second_occurrence(data, search_text, occur)
print(res)                                          # res = -1

data = []
search_text = "123"
print(f'Результаты поиска {search_text} в {data}:')
res = Find_second_occurrence(data, search_text, occur)
print(res)                                          # res = -1