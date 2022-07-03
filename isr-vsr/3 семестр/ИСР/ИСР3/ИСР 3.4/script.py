def encrypt(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet.upper()
    
    s = ''
    for symbol in text:
        if symbol in alphabet:
            s += alphabet[(alphabet.index(symbol) + 13) % len(alphabet)]
        if symbol in alphabet_upper:
            s += alphabet_upper[(alphabet_upper.index(symbol) + 13) % len(alphabet_upper)]
    return s


def main():
    text = input('Введите текст: ')
    encrypted_text = encrypt(text)
    print(encrypted_text)


if __name__ == '__main__':
    main()