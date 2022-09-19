# 2. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

import random

def candy_game(n):
    candies = 2021
    player_move = 0
    count = 0
    while candies > 0:
        if n == 0:
            player_move = input('Введите количество конфет: ')
            while True:
                try:
                    player_move = int(player_move)
                    if player_move < 1 or player_move > 28:
                        player_move = input('Введите число от 1 до 28: ')
                    else:
                        break
                except ValueError:
                    player_move = input('Введите число от 1 до 28: ')
            candies -= player_move
            print(f'Осталось конфет: {candies}')
            n = 1
            count += 1
        if n == 1:
            if candies == 2021:
                step = 4
                print(f'Ход бота: {step}')
            elif candies < 29:
                step = candies
                print(f'Ход бота: {step}')
            elif player_move == 4 and count == 1:
                step = 28
                print(f'Ход бота: {step}')
            elif player_move < 28:
                if (candies - 29) % 28 == 0:
                    step = 28 - player_move
                else:
                    step = (candies - 29) % 28
                print(f'Ход бота: {step}')
            elif player_move == 28:
                step = 28
                print(f'Ход бота: {step}')
            candies -= step
            print(f'Осталось конфет: {candies}')
            n = 0
            count += 1
    if n == 0:
        s = 'Выиграл бот'
    elif n == 1:
        s = 'Выиграл игрок'
    return s


n = random.randint(0, 1)
result = candy_game(n)
print(result)
