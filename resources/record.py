from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import RecordModel, CategoryModel
from schemas import RecordSchema, RecordQuerySchema
from sqlalchemy.exc import IntegrityError


blp = Blueprint("record", __name__, description="Operations on category")


@blp.route("/record/<string:record_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, id_of_records):
        record = RecordModel.query.get_or_404(id_of_records)
        return record


@blp.route("/record")
class RecordList(MethodView):
    @blp.arguments(RecordQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, RecordSchema(many=True))
    def get(self, **kwargs):
        id_of_user = kwargs.get("id_of_user")
        if not id_of_user:
            return abort(400, message="Need at least id_of_user to get records")

        query = RecordModel.query.filter(id_of_user == id_of_user)

        id_of_category = kwargs.get("id_of_category")
        if id_of_category:
            query = query.filter(id_of_category == id_of_category)
        return query.all()

    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, request_data):
        record = RecordModel(**request_data)

        id_of_category = request_data.get("category_id")

        category_owner_id = CategoryModel.query.with_entities(CategoryModel.owner_id).filter_by(id=id_of_category).scalar()

        if category_owner_id == request_data["user_id"] or category_owner_id is None:
            try:
                db.session.add(record)
                db.session.commit()
            except IntegrityError:
                abort(400, message="Error when creating note")
            return record
        abort(403, message="User has no access to this category")
