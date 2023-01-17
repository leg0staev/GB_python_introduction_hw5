# Задача 101 Вычислить число π c заданной точностью d

# Пример:
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001

# 3,1415926535897932384626433832795

# R = pi * D

from math import pi

PI_NUMBER = pi
print(PI_NUMBER)


def user_input() -> str:
    while True:
        try:
            accuracy_input = str(
                input('enter the accuracy value d (0.1 ≤ d ≤ 0.00000000001): '))

            if 0.00000000001 <= float(accuracy_input) <= 0.1\
                and int(accuracy_input.split('.')[1]) == 1:
                return accuracy_input

            print(accuracy_input)
            print('invalid value. try again..')
        except:
            print(accuracy_input)
            print('invalid value. try again..')


USER_ACCURACY = user_input()

ACCURASY_VALUE = len(USER_ACCURACY) - 2
result_pi = round(PI_NUMBER, ACCURASY_VALUE)
print(result_pi)
