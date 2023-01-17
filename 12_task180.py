# Задача 108 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления
# данных (модуль в отдельном файле, импортируется как библиотека)
# метод Упаковка: на вход подается текстовый файл, на выходе текстовый файл со сжатием.
# метод Распаковка: на вход подается сжатый текстовый файл, на выходе текстовый файл восстановленный.
# Прикинуть достигаемую степень сжатия (отношение количества байт сжатого к исходному).

import rle

# функция чтения строки из файла
def get_input_file(file_name: str) -> str:
    with open(f'{file_name}.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    return data

# функция записи строки в файл
def get_output_file(string: str, file_name: str) -> None:
    file = open(f'{file_name}.txt', 'w', encoding='utf-8')
    file.write(string)
    file.close()

# упаковка
text_to_encode = get_input_file('text_to_encode')
encoded_text = rle.encode(text_to_encode)
get_output_file(encoded_text, 'encoded_text')

# распаковка
text_to_decode = get_input_file('encoded_text')
decoded_text = rle.decode(text_to_decode)
get_output_file(decoded_text, 'decoded_text')

# прикидываю степень сжатия
print()
print(f'Compress ratio: \t{round(len(decoded_text) / len(encoded_text), 1)}')
