# Задача 102 Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


def UserInput() -> int:
    while True:
        try:
            number = int(input('set a natural number: '))
            if 0 < number:
                return number
            else:
                print('invalid number. try again..')
        except:
            print('invalid value. try again..')


def GetSimpleMultipliers(naturalNumber: int) -> list:
    simpleMultipliers = []
    simpleMultiplier = 2
    while simpleMultiplier <= naturalNumber:
        if naturalNumber % simpleMultiplier == 0:
            simpleMultipliers.append(simpleMultiplier)
            naturalNumber //= simpleMultiplier
            simpleMultiplier = 2
        else:
            simpleMultiplier += 1
    return simpleMultipliers


userInput = UserInput()
simpleMultipliers = GetSimpleMultipliers(userInput)

print('simple multipliers list:',*simpleMultipliers)
