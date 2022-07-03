'''
2.1 Написать программу, позволяющую выполнять подсчет слов в тексте, а также вычислять размер (в символах) каждого слова. Используйте для возвращения результатов подсчета механизм генераторов.
'''

def words_len(text):
    text = text.replace(',', ' ').replace('.', ' ').replace(';', ' ')
    print('Кол-во слов:', len(text.split()))
    for word in text.split():
        yield word + ': ' + str(len(word))


def main():
    text = input('Введите текст: ')
    for w in words_len(text):
        print(w)


if __name__ == '__main__':
    main()