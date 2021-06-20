import os
from flask import Flask

from phonebook.api import api
from phonebook.views import views

import phonebook.config.sqlite3 as sqlite3

def create_app():
    """" Flask app factory"""

    app = Flask(__name__)

    config_name = os.environ["FLASK_CONFIG"]

    config_module = f"phonebook.config.env.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    # TODO: select db type
    sqlite3.init_app(app)

    app.register_blueprint(api)
    app.register_blueprint(views)

    return app

