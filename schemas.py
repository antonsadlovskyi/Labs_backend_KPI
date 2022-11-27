from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class RecordQuerySchema(Schema):
    id_of_user = fields.Str(required=True)
    id_of_category = fields.Str()

class RecordSchema(Schema):
    id = fields.Str(dump_only=True)
    id_of_user = fields.Str(required=True)
    id_of_category = fields.Str(required=True)
    amounts = fields.Float(required=True)