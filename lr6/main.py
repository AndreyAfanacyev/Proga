"""
Разработать фрагмент программы, позволяющий получать данные о текущих курсах валют с сайта Центробанка РФ с использованием сервиса, который они предоставляют. Применить шаблон проектирования «Одиночка» для предотвращения отправки избыточных запросов к серверу ЦБ РФ (запретить вызов функции get_currencies более 1 раза в секунду). Оформить решение в виде корректно работающего приложения, реализовать тестирование и опубликовать его в портфолио.

Страница документации: https://cbr.ru/development/
"""

# http://www.cbr.ru/scripts/XML_daily.asp
import time
import requests
from datetime import datetime
from xml.etree import ElementTree as ET  # исследовать библиотеки для парсинга xml и использовать более оптимальную библиотеку для парсинга xml (если такая есть)


# синглтон позволяет обеспечивать существование только одного экземпляра класса
def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class CurrenciesList():
    def __init__(self):
        self.data_available = False # есть ли сохранённые данные
        self.t = time.time() # время выполнения запроса
        self.data = None # сохранённые данные

    def get_currencies(self, currencies_ids_lst=None):
        t = time.time() # текущее время
        
        if not self.data_available or t - self.t >= 3600:
            # выполняется максимум один запрос к серверу в секунду
            # также запрос выполняется, если нет сохранённых данных (функция запускается в первый раз)
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

            self.result = result
            self.data_available = True
            
        return self.result


# если id объектов одинаковые, то декоратор-синглтон работает правильно
# три экземпляра класса фактически указыват на один

my_cur_list = CurrenciesList()
res = my_cur_list.get_currencies(["R01090B", "R01720", "R01565"])
print(res)
print('id:', id(my_cur_list))

my_cur_list2 = CurrenciesList()
res = my_cur_list2.get_currencies(["R01090B", "R01720", "R01565"])
print(res)
print('id:', id(my_cur_list2))

print(type(CurrenciesList))

my_cur_list3 = CurrenciesList()
res = my_cur_list3.get_currencies(["R01090B", "R01720", "R01565"])
print(res)
print('id:', id(my_cur_list3))
