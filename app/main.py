class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    persons = [Person(data["name"], data["age"]) for data in people]

    for data in people:
        spouse_key = "wife" if "wife" in data else "husband" if "husband" in data else None
        if spouse_key is None:
            continue
        spouse_name = data.get(spouse_key)
        if spouse_name is None:
            continue
        person = Person.people[data["name"]]
        spouse = Person.people[spouse_name]
        setattr(person, spouse_key, spouse)

    return persons
