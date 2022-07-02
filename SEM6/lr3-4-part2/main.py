import pandas as pd

path = 'MarketingSpend.csv'

data = pd.read_csv(path) # чтение данных из файла

for col in ('Online Spend', 'Offline Spend'):
    # расчёт показателей для столбцов
    print(col + ':')
    
    print('Min:', data[col].min())
    print('Max:', data[col].max())
    print('Среднее:', data[col].mean())
    print('Медиана:', data[col].median())
