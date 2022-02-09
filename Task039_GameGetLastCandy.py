# 39. Помните игру с конфетами из модуля "Математика и Информатика"?
# Создайте такую игру для игры человек против человека
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом" (брать по OCT_m+1_K)

import random
import os


def clear():
    return os.system('cls')


def Init_game():
    clear()
    init_candys = 200
    max_candys_by_step = 28
    current_candys = init_candys
    print(f'Привет, дорогой друг! Предлагаем сыграть в увлекательную игру "Забери последнюю конфетку!" Правила простые: ' +
          f'на столе лежат {init_candys} конфет. Вы по очереди берёте несколько конфет, но не более {max_candys_by_step} штук за раз. ' +
          f'Побеждает тот, кто заберёт последнюю конфету и не оставит ничего другому игроку!')
    players = []
    bot_names = ['Василий', 'Никодим', 'Кеша', 'Вольдемар', 'Кузя', 'Гоша', 'Яша']
    print('Игрок 1, как Вас зовут?')
    players.append(input())
    bot = 'бот ' + random.choice(bot_names)
    players.append(bot)
    print(f'Отлично! И сегодня против Вас играет {bot}')

    current_player_index = 1
    while current_candys > 0:
        if current_player_index == 0:
            current_player_index = 1
        else:
            current_player_index = 0
        current_candys = Next_move(
            current_candys, max_candys_by_step, players, current_player_index)

    if current_player_index == 0:
        print(f'Ура, Вы забираете последнюю конфету! Поздравляем! Хотите, сыграем еще раз y/n?')
    else:
        print(
            f'И последнюю конфету забирает {players[current_player_index]}! В следующий раз Вам обязательно повезёт! Хотите, сыграем еще раз y/n?')
    answer = input()
    while (answer != 'y') and (answer != 'n'):
        print(f'Если хотите сыграть еще раз, нажмите: y - да, n - нет')
        answer = input()
    if answer == 'y':
        Init_game()
    else:
        exit()
    return


def Check_step(value, max_candys_by_step):
    while not value.isnumeric():
        print(f'Ошибка ввода! Введите число от 1 до {max_candys_by_step}')
        value = input('Сколько конфет Вы хотите взять? ')
    step = int(value)
    return step


def Next_move(current_candys, max_candys_by_step, players, current_player):
    if current_player == 0:
        print(f'{players[current_player]}, Ваш ход! Возьмите не более {max_candys_by_step} конфет. Всего конфет осталось: {current_candys}')
        step = Check_step(input('Сколько конфет Вы хотите взять? '), max_candys_by_step)

        while (step < 1) or (step > max_candys_by_step) or (step > current_candys):
            if step <= 0:
                print(
                    f'{players[current_player]}, количество взятых конфет должно быть больше 1!')
            if step > max_candys_by_step:
                print(
                    f'{players[current_player]}, не более {max_candys_by_step} конфет!')
            if step > current_candys:
                print(
                    f'{players[current_player]}, конфет осталось всего {current_candys}! Вы не можете взять больше! Попробуйте еще раз?')
            step = Check_step(input('Сколько конфет Вы хотите взять? '), max_candys_by_step)
    else:
        step = Player_bot(current_candys, max_candys_by_step)
        print(f'{players[current_player]} забирает {step} конфет')
    return current_candys - step


def Player_bot(current_candys, max_candys_by_step):
    step = current_candys % (max_candys_by_step + 1)
    if step < 1:
        step = random.randint(1, max_candys_by_step)
    return step


Init_game()
