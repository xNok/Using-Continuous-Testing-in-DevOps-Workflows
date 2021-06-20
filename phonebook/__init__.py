from flask import Flask
from phonebook.api import api
from phonebook.views import views

import os

def create_app(config_name):
    """" Flask app factory"""

    app = Flask(__name__)

    config_module = f"phonebook.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    app.register_blueprint(api)
    app.register_blueprint(views)

    return app

app = create_app(os.environ["FLASK_CONFIG"])