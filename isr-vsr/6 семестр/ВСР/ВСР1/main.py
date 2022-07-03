import timeit
import numba
import numpy as np
import matplotlib.pyplot as plt


def multiply(size):
    matrix1 = np.random.rand(size, size)
    matrix2 = np.random.rand(size, size)
    result = np.zeros(shape=(size, size))
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]


@numba.jit
def n_multiply(size):
    matrix1 = np.random.rand(size, size)
    matrix2 = np.random.rand(size, size)
    result = np.zeros(shape=(size, size))
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]


if __name__ == '__main__':
    values1 = []
    values2 = []

    for i in range(2, 21):
        t = timeit.timeit(lambda: multiply(i), number=100)
        values1.append(t)
    
    for i in range(2, 21):
        t = timeit.timeit(lambda: n_multiply(i), number=100)
        values2.append(t)
        
    plt.plot(range(2, 21), values1, label='Python')
    plt.plot(range(2, 21), values2, label='Numba')
    plt.title('Время вычисления произведения квадратных матриц (n=100)')
    plt.xlabel('Размерность матриц')
    plt.ylabel('Время вычисления')
    plt.legend()
    plt.grid(True)
    plt.show()
