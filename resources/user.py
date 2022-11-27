import uuid

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import users, db
from models.user import UserModel
from schemas import UserSchema
from sqlalchemy.exc import IntegrityError

blp = Blueprint("user", __name__, description="Operations on user")

@blp.route("/user/<string:id_of_user>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, id_of_user):
        user = UserModel.query.get_or_404(id_of_user)
        return user

    @blp.response(200, UserSchema)
    def delete(self, id_of_user):
        raise NotImplementedError("Not implemented for now")


@blp.route("/user")
class UserList(MethodView):

     @blp.response(200, UserSchema(many=True))
     def get(self):
         return UserModel.query.all()


     @blp.arguments(UserSchema)
     @blp.response(200, UserSchema)
     def post(self, request_data):
        user = UserModel(**request_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="User with this name already exists",
            )
        return user


