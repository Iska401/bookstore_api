from app.models import BookModel
from flask import request


class UpdateBookService:
    @staticmethod
    def update():
        data = request.get_json()
        book_model = BookModel()

        book = book_model.query.filter_by(id=data['id']).first()

        if book is not None:
            book_model.update_book(book=book, data=data)
            return {'msg': 'Book has been successfully updated'}, 200
        return {'msg': "Book was not found"}, 204