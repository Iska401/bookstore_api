from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..services import LogOutService


class Logout(Resource):
    @jwt_required()
    def delete(self):
        return LogOutService.logout()