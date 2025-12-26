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
        spouse_name = data.get("wife")
        spouse_key = "wife" if spouse_name is not None else None
        if spouse_key is None:
            spouse_name = data.get("husband")
            spouse_key = "husband" if spouse_name is not None else None
        if spouse_name is None:
            continue
        person = Person.people[data["name"]]
        spouse = Person.people[spouse_name]
        setattr(person, spouse_key, spouse)

    return persons
