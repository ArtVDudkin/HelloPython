# 20. Задать номер четверти, показать диапазоны для возможных координат

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

# string Diapazone(int number)                    // функция для определения диапазона возможных знанией по номеру координатной четверти
# {
#     string result = string.Empty;
#     if (number == 1) result = $"x\u243E (0, {int.MaxValue}], y\u243E (0, {int.MaxValue}]";   //  II   |y  I
#     if (number == 2) result = $"x\u243E [{int.MinValue}, 0), y\u243E (0, {int.MaxValue}]";   // ______|______x
#     if (number == 3) result = $"x\u243E [{int.MinValue}, 0), y\u243E [{int.MinValue}, 0)";   //       |
#     if (number == 4) result = $"x\u243E (0, {int.MaxValue}], y\u243E [{int.MinValue}, 0)";   //  III  |  IV
#     return result;
# }

# Console.WriteLine("Введите номер координатной четверти:");
# int number = Convert.ToInt32(Console.ReadLine());               // Преобразуем введенное значение в целочисленный тип
# while ( (number < 1) || (number > 4) )
# {
#     Console.WriteLine("Введенное некорректное значение. Введите номер координатной четверти от 1 до 4!");
#     number = Convert.ToInt32(Console.ReadLine());
# }

# // выводим на экран значение функции при заданном значении координатной четверти
# Console.WriteLine($"Диапазон возможных значений для {number} координатной четверти: {Diapazone(number)}"); 