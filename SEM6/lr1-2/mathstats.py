"""
Для вычисления дисперсии и ср. квадр. отклонения использовать 
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg
"""


class MathStats():
    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._mean = None
        self._max = float('-Inf')
        self._min = float('Inf')
        # чтение CSN файла
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)


    @property
    def data(self):
        # геттер, возаращает данные, считанные из CSV-файла
        return self._data


    def get_mean(self, data):
        """
        Вычисление среднего по оффлайн и онлайн тратам
        """
        # считается сумма по столбцам Offline и Online, затем делится на кол-во элементов
        # среднее арифметическое
        sums = {'offline': 0, 'online': 0}
        for _l in data:
            sums['offline'] += _l['Offline']
            sums['online'] += _l['Online']

        self._mean = (sums['offline'] / len(data), sums['online'] / len(data))

        return self._mean

    @property
    def max(self):
        # выбираются все данные по столбцам Offline и Online
        offline = [d['Offline'] for d in self._data]
        online = [d['Online'] for d in self._data]
        self._max = (max(offline), max(online)) # кортеж содержит максимальные значения обеих списков
        return self._max

    @property
    def min(self):
        # выбираются все данные по столбцам Offline и Online
        offline = [d['Offline'] for d in self._data]
        online = [d['Online'] for d in self._data]
        self._min = (min(offline), min(online)) # кортеж содержит минимальные значения обеих списков
        return self._min

    @property
    def disp(self):
        # расчёт дисперсии по формуле
        # сумма квадратов разности значения и среднего арифметического, делённая на кол-во элементов
        # отдельно по столбцам Offline и Online
        offline_mean, online_mean = self.get_mean(self._data)
        offline_ms, online_ms = 0, 0
        for _l in self._data:
            _, offline, online = _l.values()
            offline_ms += (offline - offline_mean) ** 2
            online_ms += (online - online_mean) ** 2
        self._disp = (offline_ms / len(self._data), online_ms / len(self._data))
        return self._disp

    # по аналогии — со среднем квадратичным отклонением
    @property
    def sigma_sq(self):
        # корень из дисперсии
        self._sigma_sq = (self._disp[0]**(1/2), self._disp[1]**(1/2))
        return self._sigma_sq
