import uuid

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from backpythonkpi.bl import get_records_by_filter
from backpythonkpi.db import records, categories, users

import datetime

blp = Blueprint("record", __name__, description="Operations on category")


@blp.route("/record/<string:record_id>")
class Record(MethodView):
    def get(self, id_of_records):
        try:
            return records[id_of_records ]
        except KeyError:
            abort(404, message="Record not found")


@blp.route("/record")
class RecordList(MethodView):
    def get(self):
        args = request.args.to_dict()
        id_of_user = args.get("user_id")
        if not id_of_user:
            return {"error": "Need at least id_of_user to get records"}, 400

        id_of_category = args.get("id_of_category")
        if id_of_category:
            return get_records_by_filter(
                lambda x: (
                        x["id_of_user"] == id_of_user and x["id_of_category"] == id_of_category
                )
            )
        return get_records_by_filter(lambda x: x["id_of_user"] == id_of_user)

    def post(self):
        request_data = request.get_json()
        id_of_records = uuid.uuid4().hex

        if (
                "id_of_user" not in request_data
                or "id_of_category" not in request_data
                or "amounts" not in request_data
        ):
            abort(400, message="Bad request. id_of_user, id_of_category, amounts are required.")

        if request_data["id_of_user"] not in users:
            abort(404, message="User not found")

        if request_data["id_of_category"] not in categories:
            abort(404, message="Category not found")

        record = {
            "id": id_of_records,
            **request_data,
            "time": datetime.datetime.now().strftime("%d-%m-%Y-%H:%M:%S"),
        }
        records[id_of_records] = record

        return record
