# Задача 106 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)
import random

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


def draw(name_one: str, name_two: str) -> list[str]:
    result = random.randint(1, 2)
    if result == 1:
        first_player = name_one
        second_player = name_two
    else:
        first_player = name_two
        second_player = name_one
    print(f'Начинает игру {first_player}!')
    return first_player, second_player


def sweets_game_with_player(sweets_number: int,
                         players_array: list[str]) -> None:
    move_count = 0

    while sweets_number > 0:

        if move_count % 2 == 0:
            walking_player = players_array[0]
        else:
            walking_player = players_array[1]

        while True:
            try:
                move = int(
                    input(f'{walking_player}, твой ход. Сколько конфет забираешь? => '))
                if move <= sweets_number:
                    if 0 < move <= maximum_move:
                        sweets_number -= move
                        print(f'на столе осталось {sweets_number} конфет(а)')
                        print()
                        move_count += 1
                        break
                    
                    print(
                        'Не пытайся нас обмануть! '
                        f'Можно взять не больше {maximum_move} клнфет =)')
                    print()
                else:
                    print(
                        f'на столе всего {sweets_number} конфет(а), '
                        'ни больше ни меньше взять ты просто не можешь. Назови новое число =)')
                    print()
            except:
                print('Уупс! похоже ты промахнулся по клавише. Попроруй еще раз..')
                print()

    print(
        'СТОП Игра! на столе больше нет конфет! '
        f'Победил {walking_player} за {move_count} хода(ов)!')


def sweets_game_with_bot(sweets_number: int, players_array: list) -> None:
    move_count = 0
    while sweets_number > 0:

        if move_count % 2 == 0:
            walking_player = players_array[0]
        else:
            walking_player = players_array[1]

        if walking_player != 'Компьютерный Бот':
            while True:
                try:
                    move = int(
                        input(f'{walking_player}, твой ход. Сколько конфет забираешь? => '))
                    if move <= sweets_number:
                        if 0 < move < 29:
                            sweets_number -= move
                            print(f'на столе осталось {sweets_number} конфет(а)')
                            print()
                            move_count += 1
                            break
                        
                        print(
                           'Не пытайся нас обмануть! '
                            f'Можно взять не больше {maximum_move} клнфет =)')
                        print()

                    else:
                        print(
                            f'на столе всего {sweets_number} конфет(а), '
                            'ни больше ни меньше взять ты просто не можешь. '
                            'Назови новое число =)')
                        print()
                except:
                    print(
                        'Уупс! похоже ты промахнулся по клавише. '
                        'Попроруй еще раз..')
        else:
            if sweets_number <= maximum_move:
                move = sweets_number
            else:
                # move = random.randint(1, maximumMove)
                move = int(sweets_number % (maximum_move + 1))

                if move == 0:
                    move = random.randint(1, maximum_move)

            print(f'Компьютерный бот забирает => {move} конфет(ы)')
            print()
            sweets_number -= move
            print(f'на столе осталось {sweets_number} конфет(а)')
            print()
            move_count += 1

    print(
        f'СТОП Игра! на столе больше нет конфет! Победил {walking_player} за {move_count} хода(ов)!')

print('Игра с конфетами на 2 игрока! \n\
на столе лежит 2021 конффета, но каждый игрок может взять максимум 28 штук за 1 ход. \n\
выигрывает тот, кто сделает последний ход.')
print()

sweets = int(2021)
maximum_move = int(28)

mode = get_game_mode()


if mode == 1:

    player_one = str(input('Игорк 1, представьтесь: '))
    player_two = str(input('Игорк 2, представьтесь: '))

    print('кто будет ходить первый должен определить жребий!')
    print()
    input('Нажмите Enter чтобы кинуть жребий...')
    print()

    players_list = draw(player_one, player_two)
    sweets_game_with_player(sweets, players_list)

elif mode == 2:

    player_one = str(input('Игорк, представьтесь: '))
    player_two = str('Компьютерный Бот')

    print('кто будет ходить первый должен определить жребий!')
    print()
    input('Нажмите Enter чтобы кинуть жребий...')
    print()

    players_list = draw(player_one, player_two)
    sweets_game_with_bot(sweets, players_list)
