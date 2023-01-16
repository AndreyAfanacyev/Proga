import timeit
import math

from main import integrate, integrate_async


def test_timeit(f):
    test_function = lambda: f(math.atan, 0, math.pi / 2, n_iter=10**4)
    t = timeit.timeit(test_function, number=100)
    print(f'{f.__name__}, n_iter=10**4, number=100: execution time = {t:.2f} sec.')
    
    test_function = lambda: f(math.atan, 0, math.pi / 2, n_iter=10**5)
    t = timeit.timeit(test_function, number=100)
    print(f'{f.__name__}, n_iter=10**5, number=100: execution time = {t:.2f} sec.')
    
    test_function = lambda: f(math.atan, 0, math.pi / 2, n_iter=10**6)
    t = timeit.timeit(test_function, number=100)
    print(f'{f.__name__}, n_iter=10**6, number=100: execution time = {t:.2f} sec.')


if __name__ == '__main__':
    test_timeit(integrate)
    
    test_timeit(integrate_async)
