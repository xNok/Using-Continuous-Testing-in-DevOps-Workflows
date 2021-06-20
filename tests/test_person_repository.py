import pytest
import sqlite3

from faker import Faker
from faker.providers import phone_number

from phonebook.domain.person import Person
from phonebook.repositories.memrepo import MemRepo
from phonebook.repositories.sqlite3 import SqliteRepo

@pytest.fixture(scope="class")
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

class Test_MemRepo:

    def test_repository_list_without_parameters(self, person_dicts):
        repo = MemRepo(person_dicts)

        persons = [Person.from_dict(i) for i in person_dicts]

        assert repo.list() == persons


class Test_Sqlite:

    def test_repository_list_without_parameters(self, person_dicts):
        db = sqlite3.connect(
            ":memory:",
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        with open('phonebook/config/schema.sql') as f:
            db.executescript(f.read())

        repo = SqliteRepo(db)

        persons = []

        for i in person_dicts:
            persons += [Person.from_dict(i)]
            sql =  f"INSERT INTO person (full_name, phone_number, email) VALUES ('{i['full_name']}', '{i['phone_number']}', '{i['email']}');"
            db.executescript(sql)

        assert repo.list() == persons

        db.close()
