from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resource.data_resource import DataResource


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_pyfile('./.env')
    api = Api(app)

    api.add_resource(DataResource, '/')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

