class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # reset class attribute ก่อนทุกครั้ง
    Person.people = {}

    # สร้างออบเจ็กต์ทั้งหมดก่อน
    persons = [Person(person_data["name"], person_data["age"]) for person_data in people]

    # เชื่อมคู่สมรส
    for person_data in people:
        person = Person.people[person_data["name"]]

        if "wife" in person_data:
            spouse_key = "wife"
        elif "husband" in person_data:
            spouse_key = "husband"
        else:
            continue

        spouse_name = person_data.get(spouse_key)
        if spouse_name is None:
            continue

        spouse = Person.people[spouse_name]
        setattr(person, spouse_key, spouse)

    return persons
