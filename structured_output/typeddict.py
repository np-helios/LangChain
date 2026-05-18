from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    city: str

new_person: Person = {'name': 'Nishtha', 'age': 22}

print(new_person)