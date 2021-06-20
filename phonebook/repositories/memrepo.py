from phonebook.domain.person import Person

class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self):
        return [Person.from_dict(i) for i in self.data]