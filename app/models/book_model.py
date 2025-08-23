from app import db


class BookModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def update_book(self, book, data):

        book.title = data['title']
        book.price = data['price']
        book.description = data['description']

    def delete_book(self, book_to_delete):
        db.session.delete(book_to_delete)
        db.session.commit()

    def add_book(self, data):
        """
        Это функция, которая получает книгу (JSON формат) c REST-API
        сервера, и затем добавляет его в базу данных.

        """
        book = BookModel(
            title=data['title'],
            description=data['description'],
            price=data['price']

        )

        db.session.add(book)
        db.session.commit()

