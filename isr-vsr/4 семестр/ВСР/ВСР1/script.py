import os
import csv
import json

class Writer:
    def __init__(self, fields):
        self._data = []
        self._fields = fields
        
        
    def add_data(self, value):
        for field in self._fields:
            if not value.get(field):
                raise ValueError('не задано значение поля')
        self._data.append(value)
        
        
    def save(self, filename):
        name, ext = os.path.splitext(filename)
        
        if ext[1:] == 'csv':
            try:
                with open(filename, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=self._fields)
                    writer.writeheader()
                    writer.writerows(self._data)
            except OSError as e:
                print('Ошибка при сохранении файла:', e)
                
        elif ext[1:] == 'json':
            try:
                with open(filename, 'w') as f:
                    json.dump(self._data, f)
            except OSError as e:
                print('Ошибка при сохранении файла:', e)
                
        else:
            raise ValueError('неверный тип файла')
        
        
if __name__ == '__main__':
    writer = Writer(['name', 'email'])
    writer.add_data({'name': 'user', 'email': 'user@example.com'})
    
    writer.save('users.csv')
    writer.save('users.json')