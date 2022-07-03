import json
import models

class ClientsDatabase():
    def __init__(self, filename='users_data.json'):
        self._filename = filename # имя файла
        f = open(self._filename)
        self._data = json.load(f) # список посетителей загружается из json-файла
        f.close()
       

    @property
    def clients(self):
        # выдача списка посетителей
        return self._data


    def save(self):
        f = open(self._filename, 'w')
        json.dump(self._data, f) # сохранение списка посетителей в json-файл
        f.close()


    def get_client_data(self, id):
        # получение информации о посетителе
        d = self._data[id-1] # индексы начинаются с 0, id - c 1 (см. строку 34)
        return models.client.Client(
            d['first_name'], d['last_name'], d['email'], d['city'], d['index'],  d['address']
        )
        
        
    def create_client(self, cl):
        self._data.append(cl.client)
        self.save() # сохранение данных
        id = len(self._data) # id посетителя = len (длина списка) - т.к. элемент добавляется в конец
        return id
