from Lab_1_Rest_API import app
from flask import jsonify, request
import datetime


id_of_user = 1


USERS = [
    {
        "id": 1,
        "name": "Anton",
    }
]





# GET / users
# POST /user



@app.route("/users")
def get_users():
    return jsonify({"users": USERS})


@app.route("/user", methods=['POST'])
def create_user():
    global id_of_user

    request_data = request.get_json()
    id_of_user += 1

    USERS.append({
        "id": id_of_user,
        "name": request_data['name']
    })
    return jsonify(request_data)
