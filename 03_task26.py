# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в
# целую степень B с помощью рекурсии.




def Degree(x, y: int) -> int:
    if y == 1:
        return x
    elif y != 1:
        return x * Degree(x, y-1)


while True:
    try:
        a = int(input('enter the the first number (A): '))
        b = int(input('enter the the second number (B): '))
        result = Degree(a, b)

        print(f'the number A to the power of B -> {result}')
        break

    except:
        print('oops! Incorrect input. Try again..')
