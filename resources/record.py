import uuid
import datetime

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from bl import get_records_by_filter
from db import records, categories, users
from schemas import RecordSchema, RecordQuerySchema


blp = Blueprint("record", __name__, description="Operations on category")


@blp.route("/record/<string:record_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, id_of_records):
        try:
            return records[id_of_records ]
        except KeyError:
            abort(404, message="Record not found")


@blp.route("/record")
class RecordList(MethodView):
    @blp.arguments(RecordQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, RecordSchema(many=True))
    def get(self, **kwargs):
        id_of_user = kwargs.get("id_of_user")

        if not id_of_user:
            return abort(400, message="Need at least id_of_user to get records")

        id_of_category = kwargs.get("id_of_category")
        if id_of_category:
            return get_records_by_filter(
                lambda x: (
                        x["id_of_user"] == id_of_user and x["id_of_category"] == id_of_category
                )
            )
        return get_records_by_filter(lambda x: x["id_of_user"] == id_of_user)

    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, request_data):

        if request_data["id_of_user"] not in users:
            abort(404, message="User not found")

        if request_data["id_of_category"] not in categories:
            abort(404, message="Category not found")

        id_of_records = uuid.uuid4().hex

        record = {
            "id": id_of_records,
            **request_data,
            "time": datetime.datetime.now().strftime("%d-%m-%Y-%H:%M:%S"),
        }
        records[id_of_records] = record

        return record
