import json

class PersonJsonEncoder(json.JSONEncoder):
    """ 
    Providing a class that inherits from json.JSONEncoder 
    let us use the syntax json.dumps(person, cls=PersonJsonEncoder)
    """
    def default(self, o):
        try:
            to_serialize = {
                "full_name": o.full_name,
                "phone_number": o.phone_number,
                "email": o.email
            }
            return to_serialize
        except AttributeError:
            return super().default(o)