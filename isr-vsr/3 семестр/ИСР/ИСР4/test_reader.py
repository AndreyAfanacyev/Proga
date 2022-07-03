from reader import TablePrinter
import pytest

def test_printer_1():
    printer = TablePrinter()
    table = printer.render_table()
    assert isinstance(table, str)


def test_printer_2():
    printer = TablePrinter()
    head = printer.header
    assert head == ['login', 'email']
    
    
@pytest.fixture()
def test_file(tmp_path):
    import json
    
    data = [
        {
            'name': 'user',
            'email': 'user@mailserver.org'
        }
    ]
    
    filename = tmp_path / 'data.json'
    
    with open(filename, 'w') as f:
        json.dump(data, f)
    
    return filename
    
    
def test_printer_newfile(test_file):
    printer = TablePrinter(test_file)
    head = printer.header
    assert head == ['name', 'email']


if __name__ == '__main__':
    test_printer_1()
    test_printer_2()