import bcrypt
from flask import request
from app.models import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token
from ..schemas import SignUpSchema
from marshmallow import ValidationError


class RegisterService:
    @staticmethod
    def register():
        try:

            data: dict = SignUpSchema().load(request.get_json())

        except ValidationError as err:
            return err.messages, 400

        username = data['username']
        password = data['password']

        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()

        is_registered = UserModel().query.filter_by(username=username).first()

        if is_registered is None:
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            hashed_pass = bcrypt.hashpw(bytes, salt)

            UserModel().register(username=username, password=hashed_pass.decode('utf-8'))
            return {'access_token': access_token, 'refresh_token': refresh_token}
        return {'msg': 'This account already exists. Please login to your account'}