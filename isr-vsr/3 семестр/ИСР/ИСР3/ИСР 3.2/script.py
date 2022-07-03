def main():
    substr = input("Введите подстроку для поиска: ")
    source = input("Введите исходную строку: ")
    
    pos = source.find(substr)
    if pos != -1:
        print('Подстрока найдена на позиции', pos)
    else:
        print('Подстрока не найдена')
        
main()