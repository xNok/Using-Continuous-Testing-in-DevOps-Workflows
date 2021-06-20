from phonebook.domain.person import Person
from phonebook.repositories.IRepo import RepoBase

class MemRepo(RepoBase):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def list(self):
        return [Person.from_dict(i) for i in self.data]