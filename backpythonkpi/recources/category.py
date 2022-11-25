import uuid

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint

from backpythonkpi.db import categories
from backpythonkpi.schemas import CategorySchema

blp = Blueprint("category", __name__, description="Operations on category")

@blp.route("/category/<string:id_of_category>")
class Category(MethodView):
    def get(self, id_of_category):
        return categories[id_of_category]


@blp.route("/category")
class GategoryList(MethodView):
    def get(self):
        return list(categories.values())


    @blp.arguments(CategorySchema)
    def post(self, request_data):
        id_of_category = uuid.uuid4().hex

        category = {
            "id": id_of_category,
            **request_data
        }
        categories[id_of_category] = category
        return category
