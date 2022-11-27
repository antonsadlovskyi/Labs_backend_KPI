from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    owner_id = fields.Int(required=False)

class RecordQuerySchema(Schema):
    id_of_user = fields.Int(required=True)
    id_of_category = fields.Int()

class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    id_of_user = fields.Int(required=True)
    id_of_category = fields.Int(required=True)
    amounts = fields.Float(required=True)