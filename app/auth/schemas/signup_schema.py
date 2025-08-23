from marshmallow import Schema, fields, validate


class SignUpSchema(Schema):
    username = fields.Str(validate=validate.Length(min=1, max=64))
    password = fields.Str(validate=validate.Length(min=8))
