from flask_jwt_extended import get_jwt_identity, create_access_token


class RefreshService:
    @staticmethod
    def refresh():
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity, fresh=False)

        return {'access_token': access_token}
