from flask_restful import Resource
from models import Book


class ProductList(Resource):
    def get(self):
        return Book.get_all_books(), 200

    def post(self):
        Book.add_book()
        return {"message": "Product(s) added successfully"}, 201

    