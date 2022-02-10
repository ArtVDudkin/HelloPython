# 41. Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
# *Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;


def Textformatter(input_text: str):
    res = ''
    if input_text.count('(') != input_text.count(')'):
        print('Ошибка ввода! Проверьте все ли скобки на месте...')
        exit()
    else:
        for i in range(len(input_text)):
            if (input_text[i] not in '0123456789()+-*/'):
                print('Ошибка ввода! В строке присутствуют посторонние символы, вычисление невозможно!')
                exit()
            elif (input_text[i] == '(') and (input_text[i +1] == ')'):
                print('Ошибка ввода! Пропущено выражение в скобках ()')
                exit()
            elif (input_text[i] == '-') and (input_text[i +1] == '-'):
                res += ''
            elif (input_text[i] == '+') and (input_text[i +1] == '+'):
                res += ''
            elif (input_text[i] == '*') and (input_text[i +1] == '*'):
                res += ''
            elif (input_text[i] == '/') and (input_text[i +1] == '/'):
                res += ''
            elif (input_text[i] in '+-*/') and (input_text[i +1] not in '(0123456789'):
                print('Ошибка ввода! Пропущено значение после знака')
                exit()
            else:
                res += input_text[i]
    return res


def Parse_input_data(input_text: str):
    res = ''
    input_text += '|'
    for i in range(0, len(input_text) -1):
        if input_text[i] in '+-*/':
            if (input_text[i] == '-') and (not input_text[i -1].isdigit()):
                res += input_text[i] 
            else:
                res += '|' + input_text[i] + '|'
        elif input_text[i] == '(':
            res += input_text[i] + '|'
        elif input_text[i] == ')':
            res += '|' + input_text[i]
        else:
            res += input_text[i]
    return res.split('|')


def Calc_block(znak, input_data: list):
    while input_data.count(znak[0]) + input_data.count(znak[1]) != 0:
        for i in range(len(input_data)):
            if str(input_data[i]) in znak:
                index_znak = i
                break
        left_value = float(input_data[index_znak - 1])
        right_value = float(input_data[index_znak + 1])
        if input_data[index_znak] == '*':
            res = left_value * right_value
        if input_data[index_znak] == '/':
            if right_value != 0:
                res = left_value / right_value
            else:
                print('Ошибка деления на 0!')
                exit()
        if input_data[index_znak] == '+':
            res = left_value + right_value
        if input_data[index_znak] == '-':
            if left_value == '':
                left_value = 0
            res = left_value - right_value
        input_data[index_znak - 1] = res
        del input_data[index_znak]
        del input_data[index_znak]
    return input_data


def Calc_expression(expr_list: list):
    result = 0
    while expr_list.count('(') != 0:
        for i in range(len(expr_list)):
            if (expr_list[i] == '('):
                index_left = i
            if expr_list[i] == ')':
                index_right = i
                break
        temp_li = [expr_list[x] for x in range(index_left +1, index_right)]
        temp_li = Calc_block('*/', temp_li)
        temp_li = Calc_block('+-', temp_li)
        expr_list[index_left] = temp_li[0]
        for i in range(index_right - index_left):
            del expr_list[index_left + 1]
    result = expr_list[0]
    return result


print('Введите выражение для вычисления в одну строку без пробелов')
input_text = '(' + input() + ')'

input_text = Textformatter(input_text)
list_of_elements = Parse_input_data(input_text)
result = Calc_expression(list_of_elements)
print(result)
