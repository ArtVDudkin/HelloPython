# 22. Найти расстояние между точками в пространстве 2D/3D

from cmath import sqrt


def Distance2D(x1, y1, x2, y2):
    return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2).real, 2)

def Distance3D(x1, y1, z1, x2, y2, z2):
    return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2).real, 2)


dimension = 0
while dimension not in range(2,4):
    print('Выберите размерность пространства: 2 - для 2D-пространства, 3 - для 3D-пространства')
    dimension = int(input())

if dimension == 2:
    print('Введите координаты точки A(x1,y1)')
    x1 = int(input())
    y1 = int(input())
    print('Введите координаты точки B(x2,y2)')
    x2 = int(input())
    y2 = int(input())
    print(Distance2D(x1, y1, x2, y2))

if dimension == 3:
    print('Введите координаты точки A(x1,y1,z1)')
    x1 = int(input())
    y1 = int(input())
    z1 = int(input())
    print('Введите координаты точки B(x2,y2,z2)')
    x2 = int(input())
    y2 = int(input())
    z2 = int(input())
    print(Distance3D(x1, y1, z1, x2, y2, z2))


# // функция для определения расстояния между точками в 2D пространстве
# double Distance2D(int x1, int y1, int x2, int y2)
# {      // расстояние между точками в 2D равно корень из ( (х2-х1)^2 + (y2-y1)^2 )
#     return Math.Round( Math.Sqrt( Math.Pow( (x2 - x1), 2) + Math.Pow( (y2 - y1), 2) ) , 2);
# }

# // функция для определения расстояния между точками в 3D пространстве
# double Distance3D(int x1, int y1, int z1, int x2, int y2, int z2)
# {      // расстояние между точками в 3D равно корень из ( (х2-х1)^2 + (y2-y1)^2 + (z2-z1)^2 )
#     return Math.Round( Math.Sqrt( Math.Pow( (x2 - x1), 2) + Math.Pow( (y2 - y1), 2) + Math.Pow( (z2 - z1), 2) ) , 2);
# }

# if (dimension == 2)     // код для работы с точками в 2D-пространстве
# {
#     //
#     Console.WriteLine("Введите координаты точки A(x1,y1):");
#     int x1 = Convert.ToInt32(Console.ReadLine());
#     int y1 = Convert.ToInt32(Console.ReadLine());
#     Console.WriteLine("Введите координаты точки B(x2,y2):");
#     int x2 = Convert.ToInt32(Console.ReadLine());
#     int y2 = Convert.ToInt32(Console.ReadLine());

#     // выводим на экран значение функции при заданных значениях координат Х и У
#     Console.WriteLine($"Расстояние между точками А({x1},{y1}) и В({x2},{y2}) равно {Distance2D(x1, y1, x2, y2)}");
# }

# if (dimension == 3)     // код для работы с точками в 3D-пространстве
# {
#     Console.WriteLine("Введите координаты точки A(x1,y1,z1):");
#     int x1 = Convert.ToInt32(Console.ReadLine());
#     int y1 = Convert.ToInt32(Console.ReadLine());
#     int z1 = Convert.ToInt32(Console.ReadLine());
#     Console.WriteLine("Введите координаты точки B(x2,y2,z2):");
#     int x2 = Convert.ToInt32(Console.ReadLine());
#     int y2 = Convert.ToInt32(Console.ReadLine());
#     int z2 = Convert.ToInt32(Console.ReadLine());

#     // выводим на экран значение функции при заданных значениях координат Х, У, Z
#     Console.WriteLine($"Расстояние между точками А({x1},{y1},{z1}) и В({x2},{y2},{z2}) равно {Distance3D(x1, y1, z1, x2, y2, z2)}");
# }
