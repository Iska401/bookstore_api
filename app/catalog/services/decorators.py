from app import jwt_redis_blocklist
from flask_jwt_extended import get_jwt, jwt_required
from functools import wraps


def token_required(func):
    @wraps(func)
    @jwt_required()
    def wrapper(*args, **kwargs):
        jwt_token = get_jwt()
        token_in_redis = jwt_redis_blocklist.get(jwt_token['jti'])

        if token_in_redis is not None:
            return {'msg': 'Login to your account or sign-up with your new account'}
        return func(*args, *kwargs)
    return wrapper
