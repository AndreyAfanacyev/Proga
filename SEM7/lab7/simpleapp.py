from flask import Flask
import os
import socket

app = Flask(__name__)

count = 0

@app.route('/')
def hello():
    """Дополнить возврат в html значение счетчика (счетчик инициализируется в момент запуска приложения"""
    name = os.getenv("NAME", 'world') # значение переменной окружения NAME (по умолчанию world)
    hostname = socket.gethostname() # имя хоста

    html = f"""
    <h1>Hello, {name}!</h1> 
    <b>Hostname:</b> {hostname} <br>
    <b>Count:</b> {count}
    """
    return html


@app.route('/stat')
def stat():
    # увеличивает значение счётчика на единицу и возвращает его
    global count
    count += 1
    html = f'Count: {count}'

    return html

@app.route('/about')
def about():
    html = f"""
    Задание выполнил Афанасьев Андрей
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) # запуск сервера

