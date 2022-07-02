"""
Использование декоратора
"""

import json
import requests
from xml.etree import ElementTree as ET  # исследовать библиотеки для парсинга xml и использовать более оптимальную библиотеку для парсинга xml (если такая есть)

class CurrenciesList:
    """
        aka ConcreteComponent
    """

    def get_currencies(self, currencies_ids_lst=None):
        # код из предыдущей лабораторной работы
        if currencies_ids_lst is None:
            currencies_ids_lst = [
                'R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589',
                'R01625', 'R01670', 'R01700J', 'R01710A'
            ]
            
        res = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
        cur_res_str = res.text

        result = {}

        root = ET.fromstring(cur_res_str)

        valutes = root.findall("Valute")

        for _v in valutes:
            valute_id = _v.get('ID')

            if str(valute_id) in currencies_ids_lst:
                valute_cur_val = _v.find('Value').text
                valute_cur_name = _v.find('Name').text

                result[valute_id] = (valute_cur_val, valute_cur_name)
        
        return result


class Decorator(CurrenciesList):
    """
    aka Decorator из примера паттерна
    """

    __wrapped_object: CurrenciesList = None # декорируемая функция

    def __init__(self, currencies_lst: CurrenciesList):
        self.__wrapped_object = currencies_lst # декорируемая функция

    @property
    def wrapped_object(self) -> str:
        # функция - геттер
        return self.__wrapped_object # возвращаем значение внутреннего (начинается с двух знаков подчёркивания) свойства __wrapped_object

    def get_currencies(self, currencies_ids_lst=None) -> dict:
        return self.__wrapped_object.get_currencies(currencies_ids_lst)


class ConcreteDecoratorJSON(Decorator):
    # наследует класс Decorator, и, соответственно, имеет свойство wrapped_object
    
    def get_currencies(self, currencies_ids_lst=None):
        # возвращает данные декорируемой функции в виде JSON
        # ensure_ascii - для отображения кириллицы
        return json.dumps(self.wrapped_object.get_currencies(currencies_ids_lst), ensure_ascii=False)


class ConcreteDecoratorCSV(Decorator):
    # наследует класс Decorator, и, соответственно, имеет свойство wrapped_object
    
    def get_currencies(self, currencies_ids_lst=None):
        # возвращает данные декорируемой функции в виде CSV
        currency_data = self.wrapped_object.get_currencies(currencies_ids_lst)

        if type(currency_data) is str:
            # если передана строка, то она читается как JSON
            # это нужно, чтобы можно было декорировать функцию, декорированную ConcreteDecoratorJSON
            currency_data = json.loads(currency_data)
        
        # формируем CSV - набор данных, разделённых точкой с запятой
        csv_data = "ID;Rate;Name\n"
        for currency, val in currency_data.items():
            row = [currency, *val]
            csv_data += row[0] + ';' + row[1] + '\n'
        csv_data = csv_data.rstrip()
        return csv_data        


def show_currencies(currencies: CurrenciesList):
    """
       aka client_code() 
    """

    # вызов функции get_currencies базового или декорированного объекта
    # т.е. вызов для всех вариантов одинаковый независимо от внутренного устройства компонента
    print(currencies.get_currencies())


if __name__ == "__main__":
    
    curlistdict = CurrenciesList()
    wrappedcurlist = Decorator(curlistdict)
    wrappedcurlist_json = ConcreteDecoratorJSON(curlistdict)
    wrappedcurlist_csv = ConcreteDecoratorCSV(curlistdict)
    wrappedcurlist_csv_json = ConcreteDecoratorCSV(wrappedcurlist_json) # применяем декоратор не к исходному объекту, а к ранее декорированному (см. строки 78-81)

    print('Компонент:')
    show_currencies(wrappedcurlist)
    print('Компонент, декорированный ConcreteDecoratorJSON:')
    show_currencies(wrappedcurlist_json)
    print('Компонент, декорированный ConcreteDecoratorCSV:')
    show_currencies(wrappedcurlist_csv)
    print('Компонент, декорированный ConcreteDecoratorJSON и ConcreteDecoratorCSV:')
    show_currencies(wrappedcurlist_csv_json)
