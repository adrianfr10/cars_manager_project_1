import logging

from flask_restful import Api

from .routes import cars
from .web.configuration import app


def create_app():

    with app.app_context():

        logging.basicConfig(level=logging.INFO)

        api = Api(app)

        cars.create_routing(app)

    return app
