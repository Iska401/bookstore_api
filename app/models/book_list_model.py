from app import db


class BookListDb(db.Model):
    # Создаю столбцы
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # img_path = db.Column(db.Text, nullable=False)
    # seller = db.Column()

    def get_all_books(self):
        """
        Вывод всех книг

        """
        return BookListDb().query.all()
