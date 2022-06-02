from .models import db
from flask import current_app as app
from .models import Product, product_schema, products_schema
from flask import request, jsonify


# Example
@app.route('/', methods=['GET'])
def get():
    return jsonify({ 'msg': 'Hello world!' })

@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    description = data['description']
    price = data['price']
    qty = data['qty']

    new_product = Product(name, description, price, qty)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)



