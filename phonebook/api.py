from flask import Blueprint

api = Blueprint('api',__name__)

@api.route('/api/v1/persons/<name>',methods = ['POST'])
def add_person(name):
    pass

@api.route('/api/v1/persons',methods = ['GET'])
def get_all_persons():
    pass

@api.route('/api/v1/persons/<name>',methods = ['GET'])
def get_person(name):
    pass