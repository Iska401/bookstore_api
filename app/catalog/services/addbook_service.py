from flask import request
from marshmallow import ValidationError
from app.catalog import BookSchema
from app.models import BookDb


db = BookDb()

class AddBookService:
    def add_book(self):
        try:
            data = BookSchema().load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
        db.add_book(data)
        return data, 201
