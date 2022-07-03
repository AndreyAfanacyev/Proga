import re
import csv
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def fetch_data():
    links = {
        'Выборгский район': 'https://www.bn.ru/kvartiry-vtorichka-vyborgskij-rayon/',
        'Невский район': 'https://www.bn.ru/kvartiry-vtorichka-nevskij-rayon/',
        'Пушкинский район': 'https://www.bn.ru/kvartiry-vtorichka-pushkinskij-rayon/'
    }
    
    prices = []

    for district, link in links.items():
        for page in range(1, 6):
            page_link = link
            
            if page > 1:
                page_link += f'?page={page}'
            
            res = requests.get(page_link)
            data = res.text

            soup = BeautifulSoup(data, 'html.parser')
            containers = soup.findAll('div', class_='catalog-item__container')
            for container in containers:
                catalog_price = container.find('div', class_='catalog-item__price')
                price = catalog_price.text.replace(' ', '').replace('₽', '')
                headline = container.find('div', class_='catalog-item__headline')
                square = re.findall('\d+\.\d+', headline.text)[0]
                    
                row = {'district': district, 'square': float(square), 'price': int(price)}
                prices.append(row)
                
    prices = sorted(prices, key=lambda x: x['square'])
    return prices


def save_csv(apartment_prices, filename='prices.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['district', 'square', 'price'])
        writer.writeheader()
        writer.writerows(apartment_prices)


def load_csv(filename='prices.csv'):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['square'] = float(row['square'])
            row['price'] = int(row['price'])
            data.append(row)
    return data


def plotter(apartment_prices):
    districts = set(d['district'] for d in apartment_prices)
    for district in districts:
        squares = [d['square'] for d in apartment_prices if d['district'] == district]
        prices = [d['price'] for d in apartment_prices if d['district'] == district]
        plt.scatter(squares, prices)
        plt.ticklabel_format(style='plain')
        plt.title(f'Цены на недвижимость ({district})')
        plt.xlabel('Площадь квартиры')
        plt.ylabel('Цена')
        plt.show()


if __name__ == '__main__':
    prices = fetch_data()
    save_csv(prices)

    prices = load_csv()
    plotter(prices)
