from app.extensions import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def register(self, username, password):
        user = UserModel(
            username=username,
            password=password
        )

        db.session.add(user)
        db.session.commit()

