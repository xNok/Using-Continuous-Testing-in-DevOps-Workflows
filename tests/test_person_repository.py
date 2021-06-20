import pytest
from faker import Faker
from faker.providers import phone_number

from phonebook.domain.person import Person
from phonebook.repositories.memrepo import MemRepo


@pytest.fixture
def person_dicts():
    fake = Faker()
    fake.add_provider(phone_number)

    return [
        {
            "email": fake.email(),
            "full_name": fake.name(),
            "phone_number": fake.phone_number()
        }
    for i in range(5)]


def test_repository_list_without_parameters(person_dicts):
    repo = MemRepo(person_dicts)

    rooms = [Person.from_dict(i) for i in person_dicts]

    assert repo.list() == rooms