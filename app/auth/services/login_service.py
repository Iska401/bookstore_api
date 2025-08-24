import bcrypt
from marshmallow import ValidationError
from app.models import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token
from flask import request
from ..schemas import LoginSchema


class LoginService:
    @staticmethod
    def login():
        try:
            data = LoginSchema().load(request.get_json())

            user_db = UserModel.query.filter_by(username=data['username']).first()
            password = data['password']

            is_pas_correct = bcrypt.checkpw(password.encode('utf-8'),
                                            user_db.password.encode('utf-8'))

        except ValidationError as err:
            return err.messages, 400

        if not is_pas_correct or not user_db:
            return {'msg': "the password or username is incorrect"}, 403
        else:
            username = data['username']

            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)

            return {'access_token': access_token, 'refresh_token': refresh_token}, 200





