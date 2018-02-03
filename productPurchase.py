from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('themes/bootstrap4'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('productPurchase.html')
print(template.render(title='Product Purchase'))
