import pytest
from unittest import mock
from faker import Faker
from faker.providers import phone_number

from phonebook.domain.person import Person
from phonebook.use_cases.manage_persons import list_persons

@pytest.fixture
def domain_persons():
    fake = Faker()
    fake.add_provider(phone_number)

    return [ Person(
        email=fake.email(),
        full_name=fake.name(),
        phone_number=fake.phone_number()

    ) for i in range(5)]


def test_room_list_without_parameters(domain_persons):
    repo = mock.Mock()
    repo.list.return_value = domain_persons

    result = list_persons(repo)

    repo.list.assert_called_with()
    assert result == domain_persons