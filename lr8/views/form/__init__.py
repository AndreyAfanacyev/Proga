def render_form():
    # подключение шаблонизатора
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('form.html') # загрузка шаблона
    result = template.render(title="Главная страница") # рендеринг страницы

    return result
