from chalice import Chalice
import boto3

app = Chalice(app_name='pythonwebapps')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/products')
def productListing():
	return [{'code':'1','name':'productName1','cost':30,'description':'product description','inventory_on_hand':10},{'code':'2','name':'productName2','cost':30,'description':'product description','inventory_on_hand':10},]

@app.route('/products/{code}')
def productD1(code):
	return productDetail(code)

@app.route('/products/{code}/detail',cors=True)
def productD2(code):
	return productDetail(code)

@app.route('/products/{code}/purchase',methods=['POST'],content_types=['application/x-www-form-urlencoded'])
def purchase(code):
  '''
  dynamodb = boto3.resource("dynamodb", region_name='us-east-2')
  table = dynamodb.Table('member')
  response = table.put_item(
    Item={
      'id':
      'datetime':
      'name':
      'email':
      'phone':
      'billing_address':
      'shipping_address':
      'code':
      'quatity':
    }
  )
  '''
  return request.json_body

	

def productDetail(code):
	return {'code':code,'name':'productName','cost':30,'description':'product description','inventory_on_hand':10}
