from email.utils import parseaddr # про проверки e-mail


class Client():
    def __init__(self, first_name, last_name, email, city, index, address):
        # валидация
        if not first_name: # не указано имя
            raise ValueError('Поле не может быть пустым')
        if not last_name: # не указана фамилия
            raise ValueError('Поле не может быть пустым')
        if not city: # не указан город
            raise ValueError('Поле не может быть пустым')
        if not address: # не указан адрес
            raise ValueError('Поле не может быть пустым')
        if not index.isnumeric(): # в индексе есть что-то помимо цифр
            raise ValueError('Указан неверный индекс')
        if not parseaddr(email): # указан неправильный e-mail
            raise ValueError('Указан неверный e-mail')

        # записываем полученные данные
        self.__client = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "city": city,
            "index": index,
            "address": address
        }

    @property
    def client(self):
        # информация о посетителе (свойство)
        return self.__client

