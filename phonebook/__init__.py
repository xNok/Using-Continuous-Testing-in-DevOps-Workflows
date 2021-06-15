from flask import Flask
from phonebook.api import api
from phonebook.views import views

app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(views)