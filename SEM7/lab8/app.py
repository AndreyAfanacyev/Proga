from flask import Flask, request
import os
import socket
import json
import datetime
import mysql.connector

app = Flask(__name__)

count = 0

def db_connect(db=None):
    # функция для подключения к базе данных
    if db:
        mydb = mysql.connector.connect(host='mysqldb',
                                       user='root',
                                       password='p@ssw0rd1',
                                       database=db)
    else:
        mydb = mysql.connector.connect(host='mysqldb',
                                       user='root',
                                       password='p@ssw0rd1')
    return mydb


@app.route('/')
def hello():
    name = os.getenv("NAME", 'world') # значение переменной окружения NAME (по умолчанию world)
    hostname = socket.gethostname() # имя хоста

    html = f'''
    <h1>Hello, {name}!</h1> 
    <b>Hostname:</b> {hostname} <br>
    <b>Counter value:</b> {count}
    '''
    return html


@app.route('/stat')
def stat():
    # увеличивает значение счётчика на единицу и возвращает его
    global count
    count += 1
    html = f'Count: {count}'

    return html


@app.route('/initdb')
def db_init():
    mydb = db_connect() # подключение к БД
    cursor = mydb.cursor() # получение курсора

    cursor.execute("DROP DATABASE IF EXISTS counter") # удаление таблицы, если она есть в базе данных
    cursor.execute("CREATE DATABASE counter") # создание базы данных counter
    cursor.close()

    mydb = db_connect('counter') # подключение к базе данных counter
    cursor = mydb.cursor() # получение курсора

    cursor.execute("DROP TABLE IF EXISTS logs") # удаление таблицы, если она есть в базе данных
    cursor.execute(
        "CREATE TABLE logs (datetime VARCHAR(255), cilent_info VARCHAR(255))") # создание таблицы logs
    cursor.close()

    mydb.commit()

    return 'database initialization completed'


@app.route('/addlog')
def add_logs():
    # добавление данных о посещении в таблицу logs
    mydb = db_connect('counter') # подключение к базе данных counter
    cursor = mydb.cursor() # получение курсора

    headers = str(request.headers['User-Agent']) # получение User-Agent пользователя
    data = (datetime.datetime.now(), headers) # создание кортежа с датой и User-Agent
    
    cursor.execute('INSERT INTO logs VALUES (%s, %s)', data) # добавление данных в БД
    mydb.commit() # сохранение изменений в БД
    
    cursor.close()

    return 'log added to database successfully'


@app.route('/logs')
def get_logs():
    # получение данных из таблицы logs
    mydb = db_connect('counter') # подключение к базе данных counter
    cursor = mydb.cursor() # получение курсора

    cursor.execute("SELECT * FROM logs") # запрос на получение данных из таблицы
    row_headers = [x[0] for x in cursor.description] # получение названий полей таблицы

    results = cursor.fetchall() # получение данных из таблицы
    json_data = [] # список с данными таблицы logs
    for result in results:
        json_data.append(dict(zip(row_headers, result))) # добавление строки таблицы в список

    cursor.close()

    data = json.dumps(json_data) # преобразование в JSON
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) # запуск сервера
