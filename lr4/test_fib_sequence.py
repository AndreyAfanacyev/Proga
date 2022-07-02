from fib_sequence import *
from itertools import islice # позволяет ограничивать количество получаемых элементов

def test_fib_1():
    assert fib(1) == [0, 1], "Тривиальный случай n = 1, список [0, 1]"


def test_fib_2():
    assert fib(4) == [0, 1, 1, 2, 3], "fib(4) должно быть [0, 1, 1, 2, 3]"
    
    
def test_fib_lst():
    assert list(FibonacchiLst(1)) == [0, 1, 1], 'n = 1, список [0, 1]'
    
    
def test_fib_iter():
    assert list(fib_iter(range(6))) == [0, 1, 1, 2, 3, 5], 'n = 5, список [0, 1, 1, 2, 3, 5]'
    
    
def test_fib_genn():
    assert list(islice(fib_genn(), 5)) == [0, 1, 1, 2, 3], '5 элементов, список [0, 1, 1, 2, 3]'
