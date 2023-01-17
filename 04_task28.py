# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(x, y: int) -> int:
    if y == 0:
        return x
    elif y != 0:
        return sum(x+1, y-1)


while True:
    try:
        a = int(input('enter the the first number (A): '))
        b = int(input('enter the the second number (B): '))
        result = sum(a, b)

        print(f'the sum A + B -> {result}')
        break

    except:
        print('oops! Incorrect input. Try again..')
