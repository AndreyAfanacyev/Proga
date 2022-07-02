import csv
import matplotlib.pyplot as plt

FILE = 'Retail.csv'
FILE2 = 'MarketingSpend.csv'

# Задание 1 (график для файла MarketingSpend.csv)
# чтение файла
data = []
with open(FILE2, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for _r in reader:
        row = {
            'Month': int(_r[''].split('-')[1]),
            'Offline': float(_r['Offline Spend']),
            'Online': float(_r['Online Spend']),
        }
        data.append(row)

# названия месяцев
months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# начальные значения сумм продаж по месяцам
online_month_sum = [0] * 12
offline_month_sum = [0] * 12
total_sum = []

for _l in data:
    # расчёт суммы продаж
    month = _l['Month'] - 1 # индекс в списке = номер месяца - 1
    online_month_sum[month] += _l['Online']
    offline_month_sum[month] += _l['Offline']
    
for i in range(12):
    # расчёт общей суммы Online и Offline продаж
    total_sum.append(int(online_month_sum[i] + offline_month_sum[i]))

# построение графика
fig, ax = plt.subplots()
idx = [i for i in range(12)] # индексы (значения оси Y для столбцов)
ax.invert_yaxis() # инвертирование оси Y, чтобы столбцы располагались по месяцам
online_bars = ax.barh(idx, online_month_sum) # столбцы сумм Online продаж
offline_bars = ax.barh(idx, offline_month_sum, left=online_month_sum) # столбцы сумм Offline справа от столбцов Online продаж
# надписи на столбцах Online продаж
for i, bar in enumerate(ax.patches[:12]):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_y() + bar.get_height() / 2 + 0.1,
        int(online_month_sum[i]), # преобразование к целому числу
        color='white'
    )
 # надписи на столбцах Offline продаж
for i, bar in enumerate(ax.patches[12:]):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_y() + bar.get_height() / 2 + 0.1,
        int(offline_month_sum[i]), # преобразование к целому числу
        color='white'
    )
ax.bar_label(offline_bars, total_sum) # подписи столбцов (общая сумма Online и Offline продаж по месяцам)
ax.set_xlim(0, 230000) # увеличение максимального значения оси X (чтобы помещался текст)
ax.set_yticks(range(12)) # метки по оси Y
ax.set_yticklabels(months) # надписи меток по оси Y (названия месяцев)
    
plt.show()





# Задание 2 (график для файла Retail.csv)

from datetime import datetime

# чтение файла
data = []
with open(FILE, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for _r in reader:
        row = {
            'InvoiceDate': _r['InvoiceDate'],
            'Quantity': _r['Quantity']
        }
        data.append(row)

dates = [_el['InvoiceDate'] for _el in data] # выбор дат
dates = list(set(dates)) # выбор различных значений дат
dates = [datetime.strptime(d, '%Y-%m-%d') for d in dates] # преобразование строк с датами в формат datetime (для сортировки и графика)
dates.sort() # сортировка дат
dates_str = [datetime.strftime(d, '%Y-%m-%d') for d in dates] # преобразование отсортрованных дат в текст (для поиска в наборе данных)

quantities = [] # список с объёмами продаж по месяцам

for date_str in dates_str:
    # поиск записей для каждой даты и суммирование продаж за месяц
    quantity = 0
    for _el in data:
        if _el['InvoiceDate'] == date_str:
            quantity += int(_el['Quantity'])
    quantities.append(quantity)

# построение графика
# s - размер точек
plt.scatter(dates, quantities, s=15, color='green')
plt.title('Продажи')
plt.ylabel('Кол-во проданных товаров')
plt.xlabel('Дни')
plt.show()