# 32. Дана последовательность чисел. 
# Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

data = [1, 2, 3, 5, 1, 5, 3, 10]
print(data)

def Del_duplicate_elements(data):
    out = []
    for e in data:
        if e not in out:
            out.append(e)
    return out

print(Del_duplicate_elements(data))