from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..services import RegisterService

class Refresh(Resource):
    @jwt_required(refresh=True)
    def get(self):
        return RegisterService().register()