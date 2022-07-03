'''
3.4. Реализовать программу шифрующую строку, задаваемую пользователем, с помощью алгоритма шифрования,
использующего сдвиг на определенное количество знаков (шифр Цезаря). Сдвиг задается пользователем.
'''


def encrypt(text, offset=1):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_upper = alphabet.upper()
    
    s = ''
    for symbol in text:
        if symbol in alphabet:
            s += alphabet[(alphabet.index(symbol) + offset) % len(alphabet)]
        if symbol in alphabet_upper:
            s += alphabet_upper[(alphabet_upper.index(symbol) + offset) % len(alphabet_upper)]
    return s


def main():
    text = input('Введите текст: ')
    encrypted_text = encrypt(text)
    print(encrypted_text)


if __name__ == '__main__':
   main()