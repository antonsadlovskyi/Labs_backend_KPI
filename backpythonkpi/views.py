import uuid

from backpythonkpi import app
from flask import jsonify, request
from flask_smorest import abort
import datetime


from backpythonkpi.db import users, records, categories





# GET /users
# POST /user
@app.route("/users")
def get_users():
    return jsonify(list(users.values()))


@app.route("/user", methods=['POST'])
def create_user():

    request_data = request.get_json()

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
    return jsonify(user)







# GET /categories
# POST /category
@app.route("/categories")
def get_categories():
    return jsonify(list(categories.values()))


@app.route("/category", methods=['POST'])
def create_category():
    # global id_of_category

    request_data = request.get_json()
    id_of_category = uuid.uuid4().hex

    category = {
        "id": id_of_category,
        **request_data
    }
    categories[id_of_category] = category
    return jsonify(category)











# GET /records
# POST /record
@app.route("/records")
def get_records():
    return jsonify(list(records.values()))


@app.route("/record", methods=['POST'])
def create_record():

    request_data = request.get_json()
    id_of_records = uuid.uuid4().hex

    if(
        "id_of_user" not in request_data
        and "category_id" not in request_data
        and "amounts" not in request_data
    ):
        abort(400, message="Bad request. user_id is required.")


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

    return jsonify(record)