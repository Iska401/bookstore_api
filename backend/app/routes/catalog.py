from flask import jsonify
from flask_restful import Resource
from models import Book
from app import app


class ProductList(Resource):
    def get(self):
        return [{'id': row[0], 'product_name': row[1], 'img_path': row[2], 'price': row[3], 'product_number': row[4]} for row in Book().get_all_products()]
    
    def post(self):
        Book().add_product()
        return {"message": "Product(s) added successfully"}, 201

    