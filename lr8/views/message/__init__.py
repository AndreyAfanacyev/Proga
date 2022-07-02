def render_message(msg):
    from jinja2 import Environment, FileSystemLoader, select_autoescape

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('message.html')       
    result = template.render(title="Регистрация на конференцию", message=msg)

    return result

