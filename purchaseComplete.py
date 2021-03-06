from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('themes/bootstrap4'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('purchaseComplete.html')
print(template.render(title='Purchase Complete'))
