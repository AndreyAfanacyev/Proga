from itertools import islice

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


if __name__ == '__main__':
    fib_lst = [num for num in FibonacchiLst(10)]
    print(fib_lst)
    
    fib_lst = list(islice(fib_genn(), 10))
    print(fib_lst)
