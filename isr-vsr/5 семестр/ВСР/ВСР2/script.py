'''
2.1 Разработать функцию, возвращающую список чисел ряда Фибоначчи с использованием бесконечных итераторов (модуль itertools).
'''

import itertools

def fib(n):
    fib_lst = [0, 1]
    for i in itertools.count():
        if i > 1:
            fib_lst.append(fib_lst[-2] + fib_lst[-1])
        if i > n-2:
            break
    return fib_lst

num = int(input('Введите кол-во элементов: '))
print(fib(num))