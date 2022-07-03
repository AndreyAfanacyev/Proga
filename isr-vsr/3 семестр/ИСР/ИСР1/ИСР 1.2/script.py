def calc_sum(a1, d, n):
    return (2 * a1 + d*  (n - 1)) / 2 * n

if __name__ == '__main__':
    a = int(input('a1 = '))
    d = int(input('d = '))
    n = int(input('n = '))
    if n >= 2:
        print('Сумма =', calc_sum(a, d, n))
