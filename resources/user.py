import uuid

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import users
from schemas import UserSchema

blp = Blueprint("user", __name__, description="Operations on user")

@blp.route("/user/<string:id_of_user>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, id_of_user):
        try:
            return users[id_of_user]
        except KeyError:
            abort(404, message="User not found")

    @blp.response(200, UserSchema)
    def delete(self, id_of_user):
        try:
            deleted_user = users[id_of_user]
            del users[id_of_user]
            return deleted_user

        except KeyError:
            abort(404, message="User not found")


@blp.route("/user")
class UserList(MethodView):

     @blp.response(200, UserSchema(many=True))
     def get(self):
         return list(users.values())


     @blp.arguments(UserSchema)
     @blp.response(200, UserSchema)
     def post(self, request_data):

         if "name" not in request_data:
             abort(400, message="Need name for create user")

         if request_data["name"] in [u["name"] for u in users.values()]:
             abort(400, message="Name must be unique")

         id_of_user = uuid.uuid4().hex

         user = {
             "id": id_of_user,
             **request_data,
         }

         users[id_of_user] = user
         return user


