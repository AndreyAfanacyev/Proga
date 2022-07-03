'''
3.1 Реализация графического интерфейса и формы для приложения «Гостевая книга» с возможностью сохранения данных из полей формы в файл.
'''

import json
import os
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

class GuestbookForm:
    def __init__(self):
        self.root = Tk()
        self.title = Label(text='Гостевая книга')
        self.title.grid(row=0, column=0, columnspan=2, sticky=W, padx=2, pady=2)
        self.surnameLabel = Label(text='Фамилия:')
        self.surnameLabel.grid(row=1, column=0, padx=2, pady=2)
        self.surnameEntry = Entry(width=25)
        self.surnameEntry.grid(row=1, column=1, padx=2, pady=2)
        self.nameLabel = Label(text='Имя:')
        self.nameLabel.grid(row=2, column=0, padx=2, pady=2)
        self.nameEntry = Entry(width=25)
        self.nameEntry.grid(row=2, column=1, padx=2, pady=2)
        self.emailLabel = Label(text='E-mail:')
        self.emailLabel.grid(row=3, column=0, padx=2, pady=2)
        self.emailEntry = Entry(width=25)
        self.emailEntry.grid(row=3, column=1, padx=2, pady=2)
        self.phoneLabel = Label(text='Телефон:')
        self.phoneLabel.grid(row=4, column=0, padx=2, pady=2)
        self.phoneEntry = Entry(width=25)
        self.phoneEntry.grid(row=4, column=1, padx=2, pady=2)
        self.addressLabel = Label(text='Адрес:')
        self.addressLabel.grid(row=5, column=0, padx=2, pady=2)
        self.addressEntry = Entry(width=25)
        self.addressEntry.grid(row=5, column=1, padx=2, pady=2)
        self.saveButton = Button(text='Сохранить', command=self.save_data)
        self.saveButton.grid(row=6, column=0, columnspan=2, padx=2, pady=2)
        self.root.mainloop()
        
        
    def save_data(self):
        surname = self.surnameEntry.get()
        name = self.nameEntry.get()
        email = self.emailEntry.get()
        phone = self.phoneEntry.get()
        address = self.addressEntry.get()
        
        entry = {'surname': surname, 'name': name, 'email': email, 'phone': phone, 'address': address}
        
        if not os.path.exists('guestbook.json'):
            with open('guestbook.json', 'w') as f:
                json.dump([], f)
        
        with open('guestbook.json', 'r+') as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f)
        
        showinfo(title='Гостевая книга', message='Данные сохранены.')
        
        
if __name__ == '__main__':
    GuestbookForm()