# функции сжатия и распаковки текста:

def encode(text: str) -> str:
    encode_result = ''
    count = 1
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count +=1
        if i == len(text)-2 or text[i] != text[i+1]:
            encode_result += str(count) + text[i]
            count = 1
    return encode_result


def decode(text: str) -> str:
    decode_result = ''
    count = ''
    for char in text:
        if char.isdigit():
            count += char
        else:
            decode_result += ''.join(map(str, [char for _ in range(int(count))]))
            count = ''
    return decode_result
