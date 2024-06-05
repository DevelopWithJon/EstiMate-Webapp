from flask_restful import Api
from apps.api.routes import API, TokenAPI


def create_api(app):
    api = Api(app)
    # api.add_resource(API, "/api/report", "/api/report/<int:userId>", "/api/report/<int:userId>/<string:propertyId>")
    api.add_resource(API, "/api/report/<string:token>")
    api.add_resource(TokenAPI, "/api/token/<string:username>/<string:password>")