from backpythonkpi import app
from flask_smorest import Api

from backpythonkpi.recources.user import blp as UserBlueprint
from backpythonkpi.recources.category import blp as CategoryBlueprint
from backpythonkpi.recources.record import blp as RecordBlueprint


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
api.register_blueprint(RecordBlueprint)

