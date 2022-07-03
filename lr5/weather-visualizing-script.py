# Часть 1: получение данных в формате json через API openweathermap

import time
import json
import requests

api_key = '9af33d802217f8aa391aa099feac181c'

def getweather(api_key=None):
    city, lat, lon = 'Saint Petersburg, RU', 59.57, 30.19

    # данные будут возвращаться в виде словаря с названием города и списком температур по датам
    result = dict()
    result['city'] = city
    result['temps'] = list()

    for i in range(5, 0, -1):    
        dt = int(time.time()) - 3600 * 24 * i # вычитаем количество секунд в 5 днях

        res = requests.get(
            f'http://api.openweathermap.org/data/2.5/'
            f'onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={api_key}&lang=ru&units=metric')
        
        data = res.json()
        
        # заполняем список, добавляя значения даты и температуры
        measures = [{'dt': measure['dt'], 'temp': measure['temp']} for measure in data['hourly']]
        result['temps'].extend(measures)
    
    return json.dumps(result)


weather_data = getweather(api_key)
print(weather_data)


# Часть 2: визуализация полученных данных с помощью matplotlib и типа диаграммы scatterplot.

import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as md
from datetime import datetime

def visualise_data(json_data):
    data = pandas.read_json(json_data)

    city_name = data['city'][0] # получаем название города

    dates = [datetime.fromtimestamp(d['dt']) for d in data['temps']] # преобразуем даты в формат datetime для корректного отображения на графике (ось X)
    temps = [t['temp'] for t in data['temps']] # получаем список температур (ось Y)

    # расчёт средней температуры
    average_dates = []
    average_ttemps = []
    # добавляем даты со смещением в 12 часов, чтобы точки ставились между двумя днями
    for i in range(5):
        average_dates.append(dates[i * 24 + 12])
    
    for i in range(5):
        day_temps = temps[i*24:i*24+24] # значения температуры за один день
        avg = sum(day_temps) / len(day_temps) # среднее арифметическое температуры
        average_ttemps.append(avg)

    plt.title(city_name)
    
    plt.scatter(dates, temps) # точки - значения температуры
    plt.plot(average_dates, average_ttemps, color='magenta') # линия - средние значения

    plt.show()

visualise_data(weather_data)