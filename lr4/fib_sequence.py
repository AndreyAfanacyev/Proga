from itertools import takewhile

# задание 1
def fib(n):
    """
    Список чисел ряда Фибоначчи 

    Возвращает значения не превосходящие данное n

    Например: 
    n = 1, lst = [0, 1, 1]
    n = 2, lst = [0, 1, 1, 2]
    n = 5, [0, 1, 1, 2, 3, 5]

    """
    res = [0, 1]
    if n < 0:
        return list() # для n < 0 возвращается пустой список, т.к. все элементы ряда больше 0
    elif n == 0:
        return res[:1] # первый элемент - 0
    elif n == 1:
        return res
    else:
        # добавляем новые элементы, пока очередной элемент не превысит n
        while True:
            cur_el = sum(res[len(res) - 2::]) # сумма двух последних элементов списка - новый элемент ряда
            if cur_el <= n: # если она меньше или равна n, то добавляем в список
                res.append(cur_el)
            else:
                break
        return res      


# задание 2
class FibonacchiLst:
    def __init__(self, maxval):
        self.maxval = maxval # максимальное значение, до которого заполняется список
        self.lst = [0, 1] # начальное значение списка
        self.idx = -1 # текущий индекс, на первой итерации будет равен 0

    def __iter__(self):
        return self # возвращается объект итератора

    def __next__(self): # выполняется на каждой итерации
        self.idx += 1
        if self.maxval < 0: # завершаем работу итератора, если максимальное значение меньше 0 (все элементы ряда больше 0)
            raise StopIteration()
        if self.idx == 0: # для индекса 0 возвращается первый элемент ряда
            return self.lst[0]
        else:
            if self.maxval == 0: # завершаем работу итератора, если максимальное значение равно 0, будет только значение 0
                raise StopIteration(self.idx)
            if self.idx == 1: # для индекса 1 возвращается второй элемент ряда
                return self.lst[1]
            cur_el = self.lst[0] + self.lst[1] # вычисление нового элемента
            del self.lst[0]
            self.lst.append(cur_el)
            if cur_el > self.maxval: # итератор работает до тех пор, пока текущее значение меньше или равно maxval
                raise StopIteration(self.idx)
            return self.lst[1] # новый элемент добавляется в конец списка
            

# задание 3
def fib_iter_se():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_iter(max_val):
    # возвращаются элемента до тех пор, пока очередной элемент не превысит максимальное значение
    return takewhile(lambda x: x <= max(max_val), fib_iter_se())


# задание 4
def fib_genn():
    lst = [0, 1]
    yield lst[0] # возвращается первое значение
    yield lst[1] # возвращается второе значение
    while True:
        # вычисление нового элемента
        cur_el = lst[0] + lst[1]
        del lst[0]
        lst.append(cur_el)
        yield lst[1] # возвращается новый элемент
