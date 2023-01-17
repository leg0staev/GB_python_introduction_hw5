# Задача 104. Даны два файла file1.txt и file2.txt, в каждом из которых находится запись многочлена
# (полученные в результате работы программы из задачи 103).
# Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.

# функция открытия файла и чтения многочлена из него
def FileRead(filename: str) -> str:
    with open(f'{filename}.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    return data

# функция открытия файла и записи многочлено в него
def WriteFile(string: str, filename: str):
    f = open(f"{filename}.txt", "w", encoding='utf-8')
    f.write(string)
    f.close()


# функция преведения многочленов в одинаковый вид ( + A*x*x + B*x + C =0  )
# и создания списка с членами многочлена
def GetPolinomialList(polynomial: str) -> list:
    if polynomial[0] != '-':
        polynomial = '+' + polynomial
    else:
        None
    polynomial = polynomial.replace('-x', '-1*x')
    polynomial = polynomial.replace('+x', '+1*x')
    polynomial = polynomial.replace('+', ' + ')
    polynomial = polynomial.replace('-', ' - ')
    polynomial = polynomial.replace('=0', '')
    return polynomial.split()


# функция расчета новых коэффициентов и создания сортированного словаря в котором
# ключи = значение степени, значения = новые коэффициенты многочлена
def GetPolinomialDict(polynomialList: list) -> dict:
    dataPolynom = {}
    for i in range(0, len(polynomialList)-1, 2):
        category = polynomialList[i+1].count('*')
        if polynomialList[i] == '-' and category in dataPolynom:
            dataPolynom[category] += int('-' +
                                         polynomialList[i+1].split('*')[0])
        elif polynomialList[i] == '-' and category not in dataPolynom:
            dataPolynom[category] = int(
                '-' + polynomialList[i+1].split('*')[0])
        elif polynomialList[i] == '+' and category in dataPolynom:
            dataPolynom[category] += int(polynomialList[i+1].split('*')[0])
        else:
            dataPolynom[category] = int(polynomialList[i+1].split('*')[0])

    return dict(sorted(dataPolynom.items(), key=lambda x: x[0], reverse=True))

# функция формирования итогового многочлена из словаря
def GetResultPolinomium(dictionary: dict) -> str:
    result = ''
    for category in dictionary:
        if category != 0:
            if dictionary[category] == 0:
                None
            elif dictionary[category] == 1 and result != '':
                result += '+x'
            elif dictionary[category] == 1 and result == '':
                result += 'x'        
            elif dictionary[category] == -1:
                result += '-x'
            else:
                if dictionary[category] > 1 and result != '':
                    result += '+' + str(dictionary[category])+'*x'
                else:
                    result += str(dictionary[category])+'*x'
            for _ in range(category - 1):
                result += '*x'
        else:
            if dictionary[category] > 0:
                result += '+' + str(dictionary[category]) + '=0'
            elif dictionary[category] == 0:
                result += '=0'
            else:
                result += str(dictionary[category]) + '=0'
    return result


file1 = str('file1')
file2 = str('file2')
resultFile = str('file_sum')

polynomialOne = FileRead(file1)
polynomialTwo = FileRead(file2)
print(
    f'input values of polynomials obtained from files {file1}.txt and {file2}.txt:')
print(polynomialOne)
print(polynomialTwo)
print()

polynomialOneList = GetPolinomialList(polynomialOne)
polynomialTwoList = GetPolinomialList(polynomialTwo)
print(polynomialOneList)
print(polynomialTwoList)
print()

sumList = polynomialOneList + polynomialTwoList
print(sumList)
print()

polynomialDict = GetPolinomialDict(sumList)
print(polynomialDict)
print()

resultPolinomium = GetResultPolinomium(polynomialDict)
print('the result of adding polynomials:')
print(resultPolinomium)
print()

WriteFile(resultPolinomium, resultFile)
print(f'the result is written to a file {resultFile}.txt')
