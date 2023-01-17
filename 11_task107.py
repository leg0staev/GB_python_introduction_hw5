import random

# вывод карты на экран
def print_maps() -> None:
    print(maps[0], end=' | ')
    print(maps[1], end=' | ')
    print(maps[2])
    print('--+---+--')

    print(maps[3], end=' | ')
    print(maps[4], end=' | ')
    print(maps[5])
    print('--+---+--')

    print(maps[6], end=' | ')
    print(maps[7], end=' | ')
    print(maps[8])
    print()

# сделать ход в ячейку
def step_maps(symbol: str, player_name: str) -> None:
    while True:
        try:
            step = int(input(f'{player_name} ({symbol}), твой ход: '))
            print()
            if 0 < step < 10:
                if step in maps:
                    ind = maps.index(step)
                    maps[ind] = symbol
                    break
                print(f'в данном поле уже стоит {maps[step - 1]}')
                print()
            else:
                print('нужно ввести номер поля (0-9)')
                print()
        except:
            print('Уупс! похоже ты промахнулся по клавише. Попроруй еще раз..')
            print()

# получить текущий результат игры
def get_result(list_of_players: list[str]) -> str:
    victory = ''
    free_fields = 0
    for i in victories:
        if maps[i[0]] == 'X' and maps[i[1]] == 'X' and maps[i[2]] == 'X':
            victory = list_of_players[0]
            return victory
        if maps[i[0]] == 'O' and maps[i[1]] == 'O' and maps[i[2]] == 'O':
            victory = list_of_players[1]
            return victory
    
    for i in maps:
        if str(i).isdigit():
            free_fields += 1

    if free_fields > 0:
        return victory
    victory = 'no free fields'

    return victory

# жребий
def draw(name_one: str, name_two: str) -> list[str]:
    result = random.randint(1, 2)
    
    if result == 1:
        player_1 = name_one
        player_2 = name_two
    else:
        player_1 = name_two
        player_2 = name_one
    print(f'Начинает игру {player_1}!')
    print()
    return player_1, player_2

# выбор режима игры
def get_game_mode() -> int:
    print('выберете режим игры:\n\
        1 - игра с соперником \n\
        2 - игра с компьютером')
    print()
    while True:
        try:
            game_mode = int(input('введите 1 или 2: '))
            print()
            if game_mode == 1:
                print('вы выбрали игру с соперником.')
                print()
                return game_mode
            if game_mode == 2:
                print('вы выбрали игру с компьютером.')
                print()
                return game_mode

            print('вы что то не то нажали')
            print()

        except:
            print('введите число 1 или 2..')
            print()

# поиск линии с нужным количеством X и O на победных линиях
def check_line(sum_O: int, sum_X: int):
    step = ''
    for line in victories:
        o = 0
        x = 0
        for j in range(len(victories[victories.index(line)])):
            if maps[line[j]] == 'O':
                o += 1
            elif maps[line[j]] == 'X':
                x += 1
        if o == sum_O and x == sum_X:
            for j in range(3):
                if maps[line[j]] != 'O' and maps[line[j]] != 'X':
                    step = maps[line[j]]
    return step

#выбор хода
def AI():
 
    field = ''
 
    # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
    field = check_line(2, 0)
 
    # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
    if field == '':
        field = check_line(0, 2)
 
    # 3) если 1 фигура своя и 0 чужих - ставим
    if field == '':
        field = check_line(1, 0)           
 
    # 4) центр пуст, то занимаем центр
    if field == '':
        if maps[4] != 'X' and maps[4] != 'O':
            field = 5
 
    # 5) если центр занят, то занимаем первую ячейку
    if field == '':
        if maps[0] != 'X' and maps[0] != 'O':
            field = 1

    if field == '':
        for i in maps:
            if str(i).isdigit():
                field = i
    return field



# инициализация карты
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


print('Крестики-Нолики')
print()

mode = get_game_mode()


if mode == 1:

    player_one = str(input('Игорк 1, представьтесь: '))
    player_two = str(input('Игорк 2, представьтесь: '))

    print('кто будет ходить первый должен определить жребий!')
    print()
    input('Нажмите Enter чтобы кинуть жребий...')
    print()

    players_list = draw(player_one, player_two)

    # основная программа
    game_over = False
    first_player = True

    while game_over is False:

        # 1. показываем карту
        print_maps()

        # 2. спросим у играющего куда делать ход
        if first_player is True:
            litera = 'X'
            step_maps(litera, players_list[0]) # делаем ход в указанную ячейку
        else:
            litera = 'O'
            step_maps(litera, players_list[1])


        winner = get_result(players_list) # определим победителя
        
        if winner == 'no free fields':
            game_over = True
            print_maps()
            print()
            print('Ничья! Победила дружба!')
        elif winner ==  players_list[0] or winner ==  players_list[1]:
            game_over = True
            print_maps()
            print()
            print('Победил', winner)
        else:
            game_over = False
            first_player = not(first_player)



elif mode == 2:

    player_one = str(input('Игорк, представьтесь: '))
    player_two = str('Компьютерный Бот')

    print('кто будет ходить первый должен определить жребий!')
    print()
    input('Нажмите Enter чтобы кинуть жребий...')
    print()

    players_list = draw(player_one, player_two)
   
    # Основная программа
    game_over = False
    first_player = True
    
    while game_over == False:
    
        # 1. Показываем карту
        print_maps()
        comp_step = ''
        # 2. Спросим у играющего куда делать ход
        if first_player is True:
            litera = 'X'
            if players_list[0] != 'Компьютерный Бот':
                step_maps(litera, player_one)
            else:
                comp_step = AI()
                index = maps.index(comp_step)
                maps[index] = litera
                print(f'Компьютер делает ход: {comp_step}')
                
        else:
            litera = 'O'
            if players_list[1] != 'Компьютерный Бот':
                step_maps(litera, player_one)
            else:
                comp_step = AI()
                index = maps.index(comp_step)
                maps[index] = litera
                print(f'Компьютер делает ход: {comp_step}')

        winner = get_result(players_list) # определим победителя

        if winner == 'no free fields':
            game_over = True
            print_maps()
            print()
            print('Ничья! Победила дружба!')
        elif winner ==  players_list[0] or winner ==  players_list[1]:
            game_over = True
            print_maps()
            print()
            print('Победил', winner)
        else:
            game_over = False
            first_player = not(first_player) 
