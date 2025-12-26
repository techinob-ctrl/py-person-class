class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # ✅ RESET class attribute ก่อน (สำคัญมาก)
    Person.people = {}

    # สร้างออบเจ็กต์ทั้งหมดก่อน
    persons = [Person(p["name"], p["age"]) for p in people]

    # เชื่อมคู่สมรส
    for p in people:
        person = Person.people[p["name"]]

        if "wife" in p:
            spouse_key = "wife"
        elif "husband" in p:
            spouse_key = "husband"
        else:
            continue

        spouse_name = p.get(spouse_key)
        if spouse_name is None:
            continue

        spouse = Person.people[spouse_name]
        setattr(person, spouse_key, spouse)

    return persons
