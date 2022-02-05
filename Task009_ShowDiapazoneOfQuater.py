# 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

def QuaterDiapazone(value):
    if value == 1:
        return 'x = (0, \u221E), y = (0, \u221E)' 
    elif value == 2:
        return 'x = (-\u221E, 0), y = (0, \u221E)'
    elif value == 3:
        return 'x = (-\u221E, 0), y = (-\u221E, 0)'
    else:
        return 'x = (0, \u221E), y = (-\u221E, 0)'

quater = 0
while quater not in range(1,5):
    print('Введите номер координатной четверти:')
    quater = int(input())
print(QuaterDiapazone(quater))
