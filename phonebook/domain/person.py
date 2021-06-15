import dataclasses

@dataclasses.dataclass
class Person():

    full_name: str
    phone_number: str
    email: str

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)



