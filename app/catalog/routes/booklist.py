from flask_restful import Resource, marshal_with, fields
from flask_jwt_extended import jwt_required
from ..services import token_required
from app.models import BookListDb

book_fields = {
    'title': fields.String,
    'description': fields.String,
    'price': fields.Integer
}



class BookList(Resource):
    @token_required
    @jwt_required()
    @marshal_with(book_fields)
    def get(self):
        return BookListDb().get_all_books(), 200
