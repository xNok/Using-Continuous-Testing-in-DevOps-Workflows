from flask import Blueprint, Response
import json

from phonebook.repositories.memrepo import MemRepo
from phonebook.use_cases.manage_persons import list_persons
from phonebook.serializers.person import PersonJsonEncoder

api = Blueprint('api',__name__)

@api.route('/api/v1/persons',methods = ['GET'])
def get_all_persons():
    repo = MemRepo([])
    result = list_persons(repo)

    return Response(
        json.dumps(result, cls=PersonJsonEncoder),
        mimetype="application/json",
        status=200,
    )
    pass

@api.route('/api/v1/persons/<name>',methods = ['POST'])
def add_person(name):
    pass

@api.route('/api/v1/persons/<name>',methods = ['GET'])
def get_person(name):
    pass