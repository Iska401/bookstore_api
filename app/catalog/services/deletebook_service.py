from flask import request
from app.models import BookModel


class DeleteBookService:
    @staticmethod
    def delete():
        data = request.get_json()

        title = data['title']
        book_id = data['id']

        book_to_delete = BookDb.query.filter_by(title=title, id=book_id).first()


        if book_to_delete is not None:
            return {'msg': "Book has been successfully deleted"}, 200
        return {'mag': "Book was not found"}, 204