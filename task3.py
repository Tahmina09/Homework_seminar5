# Создайте программу для игры в ""Крестики-нолики"".

first_player = ''
second_player = ''
playerpos = { 'X' : [], 'O' : []}
current_player = first_player
matrix = [' ' for i in range(9)]


def draw_board(matrix): # 
    i = 0
    print('\t-------------')
    while i < len(matrix):
        print('\t| {} | {} | {} | '.format(matrix[i], matrix[i + 1], matrix[i + 2]))
        print('\t-------------')
        i += 3

draw_board(matrix)
print('\nЭто поле для игры в "Крестики-нолики".\nЧтобы поместить Х или 0 в клеточку, укажите номер клеточки.\n')


def xo_choice(): # Выбор х или о
    
    global current_player
    global first_player
    global second_player
    
    print('\nНажимите 1, чтобы выбрать X ')
    print('Нажимите 2, чтобы выбрать O ')
    
    valid = True
    while valid:
        try: 
            choice = int(input('Первый игрок сделайте выбор: '))
        except ValueError:
            print('Некорректный ввод. Попробуйте ещё раз!')
            continue
                
        if choice == 1:
            first_player = 'O'
            second_player = 'X'
            
        elif choice == 2:
            first_player = 'X'
            second_player = 'O'
             
        else:
            print('Некорректный ввод. Попробуйте ещё раз!')
            continue
        
        if current_player == second_player: 
            current_player = first_player 
        else: 
            current_player = second_player
            
        valid = False
        
      
def que_players():     #Очередность ходов участников
    global current_player
    
    if current_player == 'X': 
        current_player = 'O'
    else:
        current_player = 'X'
  
    
def put_xo():   #Вставка и проверка х и о
    valid = True
    global current_player
    
    
    while valid == True:
        try:   
            move = int(input(f'Игрок {current_player} введите номер ячейки: '))
        except ValueError:
            print('Некорректный ввод. Попробуйте ещё раз!')
            continue
                
        if move < 1 or move > 9:
            print('Некорректный ввод. Введите число от 1 до 9!')
            
        if matrix[move - 1] != ' ':
            print('Эта ячейка занята. Попробуйте ещё раз!')
            continue
            
        else:
            if current_player == first_player:
                matrix[move - 1] = first_player
                playerpos[first_player].append(move)
            else:
                matrix[move - 1] = second_player
                playerpos[second_player].append(move)
                   
            
        draw_board(matrix)
        que_players()
        
        if is_victory() == True:
            valid = False
            break
        
            
            
def is_victory():
    global first_player
    global second_player
    
    winner = [[1, 2, 3], [1, 5, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9]]
    
    for i in winner:
        if all(j in playerpos[first_player] for j in i):
            print(f'Игрок {first_player} победил! Поздравляем!')
            return True
        elif all(k in playerpos[second_player] for k in i):
            print(f'Игрок {second_player} победил! Поздравляем!')
            return True
        else:
            if len(playerpos['X']) + len(playerpos['O']) == 9:
                print('Ничья! Победила дружба!')   
                return True
    
            
xo_choice()
put_xo()