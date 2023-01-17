# Задача 105 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import random


def UserInput() -> int:
    while True:
        try:
            number = int(input('enter the number of words in your text: '))
            if 0 < number:
                return number
            else:
                print('invalid number. try again..')
        except:
            print('invalid value. try again..')


# генератор рандомного текста из несуществующих слов
def TextGenerator(wordsNumber: int) -> str:
    resultString = ''
    baseString = 'абв'
    for _ in range(wordsNumber):
        for _ in range(random.randint(4, 7)): # количество букв в слове от 4 до 7
            resultString += baseString[random.randint(0, len(baseString)-1)]
        resultString += ' '
    return resultString

def ABVDelete(textInput: str) -> str:
    wordsArray = textInput.split()

    for word in wordsArray:
        if 'абв' in word:
            wordsArray.remove(word)
    
    resultString = ' '.join(wordsArray)

    return resultString




numberOfWords = UserInput()
print()

text = TextGenerator(numberOfWords)
print('generated text:')
print(text)
print()

newText = ABVDelete(text)
print('processed text:')
print(newText)
