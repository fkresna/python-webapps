from jinja2 import Environment, FileSystemLoader, select_autoescape
import requests,json,config
apiurl = config.API_URL
r = requests.get(apiurl+'products')
products = json.loads(r.text)

env = Environment(
    loader=FileSystemLoader('themes/bootstrap4'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('productListing.html')
print(template.render(title='Product List',products=products,apiurl=apiurl))
