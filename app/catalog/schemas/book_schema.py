from marshmallow import Schema, fields, validate


class BookSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Int(validate=validate.Range(min=1, max=1000000), required=True)

