import json
from tabulate import tabulate

class TablePrinter:
    
    def __init__(self, filename='users.json', fields=None):
        self._data = []

        try:
            with open(filename) as f:
                self._data = json.load(f)
        except FileNotFoundError:
            print('файл не найден')
        except json.decoder.JSONDecodeError:
            print('ошибка чтения JSON')
            
        if fields:
            for field in fields:
                if field not in self._data[0]:
                    raise ValueError(f'поле {field} не найдено')
    
    
    @property
    def header(self):
        header = list(self._data[0].keys())
        return header
    
    
    @property
    def data(self):
        return self._data


    def render_table(self):
        header = list(self._data[0].keys())
        data = [d.values() for d in self._data]
        return tabulate(data, header)


if __name__ == '__main__':
    printer = TablePrinter(fields=['login', 'email'])
    print(printer.render_table())
    print(printer.header)
