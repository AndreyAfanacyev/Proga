from typing import List
from mathstats import MathStats

FILE = 'Retail.csv'
FILE2 = 'MarketingSpend.csv'


def main():
    # запускающая функция
    data = read_data(FILE)
    c = count_invoice(data[:5])
    print(f'Всего инвойсов (invoices): {c}')  # 2
    c = count_invoice(data[:11])
    print(f'Всего инвойсов (invoices): {c}')  # 5
    c = count_invoice(data)
    print(f'Всего инвойсов (invoices): {c}')  # 16522

    data2 = MathStats(FILE2)
    slice_test1 = data2.data[:2]

    print(data2.get_mean(slice_test1))  # (4500.0, 2952.43)
    
    print('Min:', data2.min)
    print('Max:', data2.max)
    print('Дисперсия:', data2.disp)
    print('Стандартное отклонение:', data2.sigma_sq)

    print('Кол-во различный значений для столбца InvoiceNo:', count_different_values(data, 'InvoiceNo'))

    print('Общее количество проданного товара для stock_code = 22178:', get_total_quantity(data, 21421))


def read_data(file: str) -> List[dict]:
    # считывание данных и возвращение значений в виде списка из словарей
    import csv
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for _r in reader:
            row = _r
            data.append(row)
    return data


def count_invoice(data: List[dict]) -> int:
    count = 0
    from collections import Counter

    # вариант из задания
    '''
    invoices = []
    for _el in data:
        invoices.append(_el['InvoiceNo'])
    '''
    # переписано через генератор списка
    invoices = [_el['InvoiceNo'] for _el in data]

    count = len(Counter(invoices)) # Counter считает количество элементов и возвращает словарь
    # длина словаря - количество различных элементов
    return count


def count_different_values(data: List[dict], key: str) -> int:
    """
    Функция должна возвращать число различных значений для столбца key в списке data

    key - InvoiceNo или InvoiceDate или StockCode
    """
    values = {d[key] for d in data} # генератор словарей
    # словарь не может содержать двух одинаковых ключей, поэтому повторения не учитываются
    result = len(values) # длина словаря - количество различных элементов
    return result


def get_total_quantity(data: List[dict], stock_code: int) -> int:
    """
    Возвращает общее количество проданнорго товара для данного stock_code
    """

    # генератор списка - берутся все значения по ключу Quantity, которые соответствуют условию
    # при этом они преобразуются в int, чтобы можно было посчитать сумму
    quantities = [int(d['Quantity']) for d in data if int(d['StockCode']) == stock_code]
    result = sum(quantities) # сумма - общее количество товара
    return result


if __name__ == "__main__":
    main()
