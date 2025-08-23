from flask_jwt_extended import get_jwt
from app import jwt_redis_blocklist
from datetime import timedelta


class LogOutService:
    @staticmethod
    def logout():
        jti = get_jwt()['jti']
        jwt_redis_blocklist.set(jti, '', ex=timedelta(hours=1))
        return {'msg': 'Access token revoked'}