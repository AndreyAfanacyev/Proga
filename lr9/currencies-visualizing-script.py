import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from datetime import date, datetime
from xml.etree import ElementTree as ET

def get_currencies(currencies_ids_lst=None):
    # получение курсов валют
    res = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    cur_res_str = res.text
    result = {}

    root = ET.fromstring(cur_res_str)

    valutes = root.findall('Valute')
    for el in valutes:
        valute_id = el.get('ID')
        if str(valute_id) in currencies_ids_lst:
            valute_cur_name = el.find('Name').text
            valute_cur_val = el.find('Value').text
            result[valute_cur_name] = valute_cur_val
    return result


def get_currency_dynamics(currency_id):
    # получение динамики курса одной валюты за один год
    today = date.today().strftime('%d/%m/%Y') # текущая дата в подходящем для сервера формате
    prev_year = date.today().replace(year=date.today().year-1).strftime('%d/%m/%Y') # дата для прошлого года в подходящем для сервера формате
    
    res = requests.get(f"http://www.cbr.ru/scripts/XML_dynamic.asp"
                       f"?date_req1={prev_year}&date_req2={today}&VAL_NM_RQ={currency_id}")
    cur_res_str = res.text

    result = {}

    root = ET.fromstring(cur_res_str)

    records = root.findall('Record')
    for el in records:
        record_date = el.get('Date')
        record_value = el.find('Value').text
        result[record_date] = record_value

    return result

# TODO 0 
# Вывести на графике 10 валют (получить по кодам валюты из ЦБС)

currencies = ['R01239', 'R01235', 'R01035', 'R012235', 'R01239', 'R01020A', 'R01100', 'R01215', 'R01370', 'R01775']
cur_vals = get_currencies(currencies)
objects = cur_vals.keys()
y_pos = np.arange(len(objects))

# TODO #1 переписать лямбда-функцию из следующей строки через list comprehension 
# или генераторы списков (как мы их называем)

values = [float(x.replace(',', '.')) for x in cur_vals.values()] # заменяем запятые в числах на точки

# TODO #2 

#  Подписи должны быть у осей (x, y), у графика, у «рисок» (тиков), 
# столбцы должны быть разных цветов с легендой

for i in range(len(objects)):
    # добавление стобцов диаграммы
    plt.bar(y_pos[i], values[i])
plt.xlabel('валюта')
plt.ylabel('курс')
plt.title('Курсы валют')
# bbox_to_anchor - перемещение легенды графика
# https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
plt.legend(objects, bbox_to_anchor=(1.1, 1.05))
plt.show()

# TODO #3 

# Нарисовать отдельный график с колебанием одной (выбранной вами) валюты
# (получить данные с сайта ЦБ за год) и отобразить его наиболее 
# оптимальным образом (типом графика)

currency_dynamics = get_currency_dynamics('R01239')
records_dates = [datetime.strptime(x, '%d.%m.%Y') for x in currency_dynamics.keys()] # преобразуем даты из строк в формат datetime для корректного отображения на графике (ось X)
records_values = [float(x.replace(',', '.')) for x in currency_dynamics.values()] # заменяем запятые в числах на точки

plt.plot(records_dates, records_values)
plt.xlabel('дата')
plt.ylabel('курс')
plt.title('Динамика курса')
plt.show()

# TODO #4 

# Отобразить это на одном изображении (2 графика)

fig, axs = plt.subplots(2)
for i in range(len(objects)):
    axs[0].bar(y_pos[i], values[i])
# https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
axs[0].legend(objects, bbox_to_anchor=(1.1, 1.05))
axs[1].plot(records_dates, records_values)
plt.show()