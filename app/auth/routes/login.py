from flask_restful import Resource
from ..services.login_service import LoginService


class Login(Resource):
    def post(self):
        return LoginService().login()
