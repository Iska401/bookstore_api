from flask_restful import Resource
from ..services import RegisterService

class RegisterUser(Resource):
    def post(self):
        return RegisterService().register()