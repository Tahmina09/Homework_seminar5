# b) Подумайте как наделить бота ""интеллектом""

from random import randint

num_of_sweets = 2021
get_sweeets = 0
player = 0
bot = 0
select_player = randint(1, 2)


def start_game():
    global select_player
    
    print('Условие задачи: На столе лежит 2021 конфета. Играют игрок и бот делая ход друг после друга.\n Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n Все конфеты оппонента достаются сделавшему последний ход.')
    while num_of_sweets > 28:
        if select_player == 1:
            print('Ход первого игрока!')
            the_player()
            select_player = False
            print()
        else:
            print('Ход бота!')
            bot_player()
            select_player = True
            print()
    else:
        if select_player == 1:
            print('Выиграл игрок! Все конфеты достаются игроку')
        else:
            print('Выиграл бот! Все конфеты достаются боту')
            
            
def bot_player():
    global num_of_sweets
    global get_sweeets
    global bot
    
    if num_of_sweets % 29 != 0:
        bot_get = num_of_sweets % 29
    else:
        bot_get = randint(1, 28)
        
    print(f'Осталось {num_of_sweets} конфет. Бот взял {bot_get} конфет.')
    
    num_of_sweets -= bot_get
    get_sweeets += bot_get
    bot += bot_get
    
def the_player():
    global num_of_sweets
    global get_sweeets
    global player
    
    take1 = int(input(f'Осталось {num_of_sweets} конфет. Сколько конфет хотите взять? '))
    if take1 > 28 or take1 <= 0 or num_of_sweets < take1:
        print('Попробуйте ещё раз! ')   
        take1 = int(input('Сколько конфет хотите взять? '))
    
    num_of_sweets -= take1
    get_sweeets += take1
    player += take1
    
start_game()