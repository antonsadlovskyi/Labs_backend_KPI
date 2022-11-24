import uuid

from backpythonkpi import app
from flask import jsonify, request
from flask_smorest import abort, Api
import datetime


from backpythonkpi.db import users, records, categories

from backpythonkpi.recources.user import blp as UserBlueprint
from backpythonkpi.recources.category import blp as CategoryBlueprint


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Finance REST API"
app.config["API_VERSION"] = 'v1'
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npn/swagger-ui-dist/"


api = Api(app)

api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)





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