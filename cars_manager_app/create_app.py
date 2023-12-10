import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from flask_restful import Api

from .email.configuration import MailConfig
from .routes.cars import cars_grouped_bp, most_expensive_bp
from .routes.cars import create_routing
from .web.configuration import app


def create_app():

    with app.app_context():

        # ----------------------------------------------------------------------
        # REST API CONFIGURATION
        # ----------------------------------------------------------------------
        logging.basicConfig(level=logging.INFO)
        api = Api(app)
        create_routing(app)
        # ----------------------------------------------------------------------
        #  ENVIRONMENT VARIABLES CONFIGURATION
        # ----------------------------------------------------------------------
        ENV_FILENAME = ".env"
        ENV_PATH = Path.cwd().absolute().joinpath(f'{ENV_FILENAME}')
        load_dotenv(ENV_PATH)
        # ----------------------------------------------------------------------
        #  EMAIL CONFIGURATION
        # ----------------------------------------------------------------------
        app.config.update(dict(

            DEBUG=True,
            MAIL_SERVER='smtp.gmail.com',
            MAIL_PORT=587,
            MAIL_USE_TLS=True,
            MAIL_USE_SSL=False,
            MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
            MAIL_PASSWORD=os.getenv("MAIL_PASSWORD")
        ))

        MailConfig.init(app)

        # ----------------------------------------------------------------------
        # GLOBAL EXCEPTION HANDLER CONFIGURATION
        # ----------------------------------------------------------------------
        @app.errorhandler(Exception)
        def handle_error(error: Exception):
            error_message = error.args[0]
            return {'message': error_message}, 500

        # ----------------------------------------------------------------------
        # BLUEPRINTS CONFIGURATION
        # ----------------------------------------------------------------------
        app.register_blueprint(cars_grouped_bp)
        app.register_blueprint(most_expensive_bp)


    return app
