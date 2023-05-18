from .web.configuration import app
from .routes import cars


from flask_restful import Api

import logging


def create_app():

    with app.app_context():

        logging.basicConfig(level=logging.INFO)

        api = Api(app)

        cars.create_routing(app)

    return app
