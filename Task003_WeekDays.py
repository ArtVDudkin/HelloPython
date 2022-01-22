# 3. По заданному номеру дня недели вывести его название

def Dayweek(index):
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return days[index - 1]

day_number = -1
while day_number not in range(1,8):
    print('Введите номер дня недели')
    day_number = int(input())
print(Dayweek(day_number))    