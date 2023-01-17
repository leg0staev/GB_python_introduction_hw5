# Задача 103 Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

# Пример:  k=2

# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0
# x*x + 5 = 0
# 10*x*x = 0

import random


def UserInput() -> int:
    while True:
        try:
            number = int(input('set polinomial degree: '))
            if 0 < number:
                return number
        
            print('invalid degree. try again..')
        except:
            print('invalid value. try again..')


def GetPolinomial(degree: int) -> str:
    k = degree
    polynomial = str('')
    conastanta = random.randint(0, 10)

    for i in range(degree):
        randomSign = random.choice(['+', '-'])
        if i == 0:
            ratio = random.randint(1, 10)

            if ratio == 1:
                if randomSign == '+':
                    polynomial += 'x'
                else:
                    polynomial += '-x'

            else:
                if randomSign == '+':
                    polynomial += str(ratio) + '*x'
                else:
                    polynomial += '-' + str(ratio) + '*x'
        else:
            ratio = random.randint(0, 10)
            if ratio == 0:
                continue
            
            if ratio == 1:
                polynomial += randomSign + 'x'
            else:
                polynomial += randomSign + str(ratio) + '*x'

        while k - i - 1 > 0:
            polynomial += '*x'
            k -= 1
        k = degree

    if conastanta == 0:
        polynomial += '=0'
    else:
        polynomial += random.choice(['+', '-']) + str(conastanta) + '=0'

    return polynomial

def WriteFile(string: str, filename: str) -> None:
    f = open(f"{filename}.txt", "w")
    f.write(string)
    f.close()


degree = UserInput()
polynomial = GetPolinomial(degree)

print(polynomial)
WriteFile(polynomial, 'file2')
