from phonebook.domain.person import Person
from phonebook.repositories.IRepo import RepoBase

from sqlite3 import Connection

class SqliteRepo(RepoBase):
    def __init__(self, db: Connection):
        super().__init__()
        self.db = db

    def list(self):

        result = self.db.execute(
            'SELECT * FROM person'
        ).fetchall()

        return [Person(i[1], i[2], i[3]) for i in result]