# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

def CheckQuater(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0


print('Введите координаты х и у')
x = int(input())
y = int(input())
if x == 0 or y == 0:
    print('Ошибка ввода: обе координаты не должны быть равны 0!')
else:
    print(CheckQuater(x, y))
