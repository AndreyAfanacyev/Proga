import functools

def calc_log(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = func(*args)
        with open('calc.log', 'a') as f:
            f.write('{} {} {} = {}\n'.format(args[0], args[2], args[1], result))
        return result
    
    return wrapper


@calc_log
def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op =='/':
        return a / b


if __name__ == '__main__':
    a = int(input('Введите первое число: '))
    b = int(input('Введите первое число: '))
    op = input('Выберите действие: ')
    
    result = calc(a, b, op)
    print(result)
