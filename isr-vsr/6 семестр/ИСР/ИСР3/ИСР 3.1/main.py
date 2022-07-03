def solve(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + d ** (1/2)) / (2*a)
        x2 = (b + d ** (1/2)) / (2*a)
        return (x1, x2)
    elif d == 0:
        x = -b / (2*a)
        return x
    else:
        return


def solver():
    print('Введите коэффициенты уравнения ax^2+bx+c:')
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    
    result = solve(a, b, c)
    
    if result:
        if type(result) is tuple:
            print('x1 = {}, x2 = {}'.format(*result))
        else:
            print('x = {}'.format(result))
    else:
        print('уравнение не имеет корней')
        
        
if __name__ == '__main__':
    solver()