# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

from random import randint

num_of_sweets = 2021
get_sweeets = 0
player_1 = 0
player_2 = 0
select_player = randint(1, 2)


def start_game():
    global select_player
    
    print('Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n Все конфеты оппонента достаются сделавшему последний ход.')
    while num_of_sweets > 28:
        if select_player == 1:
            print('Ход первого игрока!')
            first_player()
            select_player = False
            print()
        else:
            print('Ход второго игрока!')
            second_player()
            select_player = True
            print()
    else:
        if select_player == 1:
            print('Выиграл первый игрок! Все конфеты достаются первому игроку')
        else:
            print('Выиграл второй игрок! Все конфеты достаются второму игроку')

            

def first_player():
    global num_of_sweets
    global get_sweeets
    global player_1
    
    take1 = int(input(f'Осталось {num_of_sweets} конфет. Сколько конфет хотите взять? '))
    if take1 > 28 or take1 <= 0 or num_of_sweets < take1:
        print('Попробуйте ещё раз! ')   
        take1 = int(input('Сколько конфет хотите взять? '))
    
    num_of_sweets -= take1
    get_sweeets += take1
    player_1 += take1
    
def second_player():
    global num_of_sweets
    global get_sweeets
    global player_2
    
    take2 = int(input(f'Осталось {num_of_sweets} конфет. Сколько конфет хотите взять? '))
    if take2 > 28 or take2 <= 0 or num_of_sweets < take2:
        print('Попробуйте ещё раз! ')   
        take2 = int(input('Сколько конфет хотите взять? '))
    
    num_of_sweets -= take2
    get_sweeets += take2
    player_2 += take2



start_game()