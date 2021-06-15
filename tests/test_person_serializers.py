import json
import uuid

from phonebook.serializers.person import PersonJsonEncoder
from phonebook.domain.person import Person

def test_serialize_domain_person():

    person = Person(
        email="foo.bar@buzz.com",
        full_name="Foo Bar",
        phone_number="555-555-5555"
    )

    expected_json = f"""
        {{
            "full_name": "Foo Bar",
            "phone_number": "555-555-5555",
            "email": "foo.bar@buzz.com"
        }}
    """

    json_person = json.dumps(person, cls=PersonJsonEncoder)

    assert json.loads(json_person) == json.loads(expected_json)