'''
4.1 Написать программу, в которой пользователь вводит число от 0 до 9 включительно, а программа выводит название введённого числа, а если второй входной аргумент type имеет значение bin, oct, hex, то функция преобразует это число в бинарную, восьмеричную или шестнадцатеричную форму. Предусмотреть проверку корректности введённого пользователем значения. При реализации используемые библиотеки должны находиться в виртуальном окружении (использовать virtualenv).
'''

def number_form(number, num_type=''):
    if type(number) is not int:
        raise TypeError('number должно быть целым числом')
    if number not in range(0, 10):
        raise ValueError('число должно входить в диапазон [0; 9]')
    if num_type:
        if num_type == 'bin':
            return format(number, 'b')
        elif num_type == 'oct':
            return format(number, 'o')
        elif num_type == 'hex':
            return format(number, 'x')
        else:
            raise ValueError('num_type не равен bin, oct или hex')
    
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    n = nums[number]
    return n


if __name__ == '__main__':
    n = int(input('Введите число: '))
    print(number_form(n))