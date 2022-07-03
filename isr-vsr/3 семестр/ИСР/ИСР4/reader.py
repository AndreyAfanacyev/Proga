import json
from tabulate import tabulate

class TablePrinter:
    
    def __init__(self, filename='users.json'):
        self._data = []

        with open(filename) as f:
            self._data = json.load(f)
    
    
    @property
    def header(self):
        '''
        >>> t.header
        ['login', 'email']
        '''
        header = list(self._data[0].keys())
        return header


    def render_table(self):
        '''
        >>> type(t.render_table())
        <class 'str'>
        '''
        header = list(self._data[0].keys())

        data = [d.values() for d in self._data]

        return tabulate(data, header)


if __name__ == '__main__':
    printer = TablePrinter()
    print('Table:')
    print(printer.render_table())
    print('Header:')
    print(printer.header)
    
    import doctest
    doctest.testmod(extraglobs={'t': printer})

