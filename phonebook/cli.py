from phonebook.repositories.memrepo import MemRepo
from phonebook.use_cases.manage_persons import list_persons

repo = MemRepo([])
result = list_persons(repo)

print(result)