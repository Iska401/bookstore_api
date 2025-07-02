from flask_sqlalchemy import SQLAlchemy
from flask import request
from run import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Book(db.Model):
    # Создаю столбцы
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    img_path = db.Column(db.Text, nullable=False)
    # seller = db.Column()

    @classmethod
    def add_book(cls):
        """
        Это функция, которая получает книгу (JSON формат) c REST-API
        сервера, и затем добавляет его в базу данных.
        
        """
        data = request.get_json()
        book = cls(
            title=data['title'],
            price=data['price'],
            description=data['description']
        )

        db.session.add(book)
        db.session.commit()

    # def delete_book():
    #     book_to_delte = db.query.get()

    @classmethod
    def get_all_books(cls):
        """
        Вывод всех книг

        """
        books = cls.query.all()
        return [{'id': book.id(), 'title': book.title(), 'price': book.price(), 'description': book.description()} for book in books]
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
