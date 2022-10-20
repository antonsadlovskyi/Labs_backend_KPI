from Lab_1_Rest_API import app
from flask import jsonify, request
import datetime




id_of_user = 1
id_of_category = 1
id_of_records = 1



USERS = [
    {
        "id": 1,
        "name": "Anton",
    }
]
CATEGORIES = [
    {
        "id": 1,
        "name": "Food",
    }
]
RECORDS = [
    {
        "id": 1,
        "id_of_user": 1,
        "id_of_category": 1,
        "time": datetime.datetime.now().strftime("%d-%m-%Y-%H:%M:%S"),
        "amounts": 100,
    }
]






# GET /users
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







# GET /categories
# POST /category
@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route("/category", methods=['POST'])
def create_category():
    global id_of_category
    id_of_category += 1

    request_data = request.get_json()

    CATEGORIES.append({
        "id": id_of_category,
        "name": request_data['name']
    })
    return jsonify(request_data)











# GET /categories
# POST /category
@app.route("/records")
def get_records():
    return jsonify({"records": RECORDS})


@app.route("/record", methods=['POST'])
def create_record():
    global id_of_records
    id_of_records += 1

    request_data = request.get_json()
    #
    # time = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M:%d")

    RECORDS.append({
        "id": id_of_records,
        "id_of_user": 1,
        "id_of_category": 1,
        "time": datetime.datetime.now().strftime("%d-%m-%Y-%H:%M:%S"),
        "amounts": 100,
    })
    return jsonify(request_data)