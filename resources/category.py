import uuid

from flask.views import MethodView
from flask_smorest import Blueprint

from db import categories
from schemas import CategorySchema

blp = Blueprint("category", __name__, description="Operations on category")

@blp.route("/category/<string:id_of_category>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, id_of_category):
        return categories[id_of_category]


@blp.route("/category")
class GategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return list(categories.values())


    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, request_data):
        id_of_category = uuid.uuid4().hex

        category = {
            "id": id_of_category,
            **request_data
        }
        categories[id_of_category] = category
        return category
