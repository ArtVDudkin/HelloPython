# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

def CheckQuater(data):
    x = data[0]
    y = data[1]
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


print('Введите координаты точки х и у через пробел')
coord = list(map(int,input().split()))
if coord[0] == 0 and coord[1] == 0:
    print(f'Точка ({coord[0]}, {coord[1]}) находится в центре системы координат!')
elif coord[0] == 0 and coord[1] != 0:
    print(f'Точка ({coord[0]}, {coord[1]}) лежит на оси У')
elif coord[0] != 0 and coord[1] == 0:
    print(f'Точка ({coord[0]}, {coord[1]}) лежит на оси X')
else:
    print(f'Точка ({coord[0]}, {coord[1]}) находится в координатной четверти {CheckQuater(coord)}')
