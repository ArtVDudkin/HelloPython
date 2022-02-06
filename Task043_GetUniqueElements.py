# 43. Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

data = [1, 2, 3, 5, 1, 5, 3, 10]
print(data)

def Get_unique_elements(input_data):
    out_data = []
    for e in input_data:
        if input_data.count(e) == 1:
            out_data.append(e)
    return out_data

unique_list = Get_unique_elements(data)
print(unique_list)
