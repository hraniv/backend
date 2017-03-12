from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    date_of_birth = fields.Date()

