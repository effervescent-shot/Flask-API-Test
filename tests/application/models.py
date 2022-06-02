from flask_marshmallow import Marshmallow
from . import db

ma = Marshmallow()

class Product(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

# Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
    


