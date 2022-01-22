# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.

def IsDevider(value_1, value_2):
    return (value_1 % value_2 == 0)


def FindReminder(value_1, value_2):
    return value_1 % value_2


print('Введите число и его предполагаемый делитель')
num = int(input())
devider = int(input())
if IsDevider(num, devider):
    print(True)
else:
    print(FindReminder(num, devider))
