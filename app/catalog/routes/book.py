from ..services import (UpdateBookService, token_required,
                        DeleteBookService, AddBookService,
                        )
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.models import BookModel
from flask import request

class Book(Resource):
    @jwt_required()
    @token_required
    def update(self):
        return UpdateBookService().update()

    @jwt_required()
    @token_required
    def get(self):
        return BookModel().query.filter_by(id=request).first(), 200

    @jwt_required()
    @token_required
    def delete(self):
        return DeleteBookService().delete()

    @jwt_required()
    @token_required
    def post(self):
        return AddBookService().add_book()