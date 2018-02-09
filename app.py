from chalice import Chalice
import boto3
import urllib.parse as urlparse
import datetime
import json

app = Chalice(app_name='pythonwebapps')
app.debug=True
dynamodb = boto3.resource("dynamodb", region_name='us-east-1')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/products')
def productListing():
  table = dynamodb.Table('product')
  try:
    response = table.scan()
  except ClientError as e:
      print(e.response['Error']['Message'])
  else:
    item = response
    return item['Items']

@app.route('/products/{code}')
def productD1(code):
	return productDetail(code)

@app.route('/products/{code}/detail',cors=True)
def productD2(code):
	return productDetail(code)

@app.route('/products/{code}/purchase',methods=['POST'],content_types=['application/x-www-form-urlencoded'])
def purchase(code):
  parsed = app.current_request.raw_body.decode()
  querys = parsed.split("&")
  var = {}
  for val in querys:
    temp=val.split("=")
    var[temp[0]] = temp[1]

  now = datetime.datetime.now()

  table = dynamodb.Table('purchase')
  response = table.put_item(
    Item={
      'date': now.date().strftime('%m/%d/%Y'),
      'name': var['cName'],
      'email': var['cEmail'],
      'phone': var['cPhone'],
      'billing_address': var['cBilling'],
      'shipping_address': var['cShipping'],
      'code': var['code'],
      'quantity': var['quantity']
    }
  )
  inv = int(int(var['inventory_on_hand']) - int(var['quantity']))
  print(inv)
  response2 = table.update_item(
    TableName='product',
    Key={'code':var['code']},
    UpdateExpression="set inv_on_hand = :i",
    ExpressionAttributeValues={':i':inv}
  )
  return "Thank you, your purchase has been sucessfull."
  
def productDetail(code):
  table = dynamodb.Table('product')
  product = table.get_item(Key={'code':code})
	# return {'code':code,'name':'productName','cost':30,'description':'product description','inventory_on_hand':10}
  return product['Item']