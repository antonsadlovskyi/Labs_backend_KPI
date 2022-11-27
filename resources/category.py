import uuid

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import CategoryModel
from schemas import CategorySchema

from sqlalchemy.exc import IntegrityError

blp = Blueprint("category", __name__, description="Operations on category")

@blp.route("/category/<string:id_of_category>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, id_of_category):
        category = CategoryModel.query.get_or_404(id_of_category)
        return category


@blp.route("/category")
class GategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()


    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, request_data):
        category = CategoryModel(**request_data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="User with this name already exists",
            )
        return category

