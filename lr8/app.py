import io
import base64
import qrcode
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from json_db import *

def get_qrcode_page(client_id, server_port):
    # генерация URL на страницу информации о пользователе
    url = ''.join(['localhost', ':', str(server_port), f'/user/{client_id}'])
    buffer = io.BytesIO() 
    img = qrcode.make(url)
    img.save(buffer, format='PNG')
    result = 'data:image/png;base64,' + base64.b64encode(buffer.getvalue()).decode('utf-8') 

    # подключение шаблонизатора
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('qr_code.html') # шаблон страницы
    result = template.render(img=result)

    return result

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        import views.client as client_view
        import views.form as form_view
        import views.message as msg_view

        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()

        result = ''

        if self.path == '/':
            result = form_view.render_form() # форма регистрации
        elif self.path[:11] == '/registered':
            clients = db.clients
            result = client_view.render_clients(clients) # список зарегистрированных посетителей
        elif self.path[:6] == '/user/':
            # вывод информации о посетителе с заданным id
            try:
                id = int(self.path[6:])
                cl = db.get_client_data(id)
                result = client_view.render_client(cl)
            except:
                result = msg_view.render_message('Неправильный id пользователя')

        result = bytes(result, 'utf-8')

        self.wfile.write(result)


    def do_POST(self):
        import models
        import views.message as msg_view

        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        params = str(body, 'utf-8') # данные формы (переданные в теле POST-запроса) получены в виде строки
        data = parse_qs(params, keep_blank_values=True) # преобразование данных в словарь
        data = {k: v[0] for k, v in data.items()}

        try:
            client = models.client.Client(
                data['firstname'], data['lastname'], data['email'], data['city'], data['index'], data['address']
            )
            user_id = db.create_client(client) # добавляем информацию в файл json
            result = get_qrcode_page(user_id, self.server.server_port) # создание QR-кода
        except ValueError as e:
            result = msg_view.render_message(str(e))  # рендеринг страницы с сообщением (модуль message_view)

        result = bytes(result,'utf-8') # преобразование содержимого HTML страницы в utf-8

        self.wfile.write(result) # выдача страницы пользователю


db = ClientsDatabase() # данные хранятся в JSON
# код для работы с файлом находится в модуле json_db.py

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()  # запуск сервера