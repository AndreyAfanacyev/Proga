'''
2.3. Разработать программу, которая для заданного количества значений возвращала бы список из уникальных элементов, содержащихся во входном наборе значений. Используйте упаковку и распаковку элементов.
'''

import random

def main():
    values = [random.randint(1, 5) for _ in range(10)]
    print('Values:', values)
    unique_values = list(set(values))
    print('Unique values:', *unique_values)
    
    
if __name__ == '__main__':
    main()