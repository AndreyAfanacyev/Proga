def calc_square(a, b, c):
    p = (a + b + c) / 2
    result = (p * (p-a) * (p-b) * (p-c)) ** (1/2)
    return result
    
    
def main():
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    sq = calc_square(a, b, c)
    print('Площадь треугольника:', sq)


if __name__ == '__main__':
    main()