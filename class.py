class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"

def serialize_person(person_obj):
    return f"Name: {person_obj.name}, Age: {person_obj.age}"

def deserialize_person(text_line):
    parts = text_line.strip().split(", ")
    name = parts[0].split(": ")[1]
    age = int(parts[1].split(": ")[1])
    return Person(name, age)

if __name__ == "__main__":
    p1 = Person("Leri", 16)
    print("1. საწყისი ობიექტი (p1):", p1)

    serialized_data = serialize_person(p1)
    print("2. სერიალიზებული ტექსტი:", serialized_data)

    filename = "person_data.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(serialized_data)
    print(f"3. მონაცემები წარმატებით ჩაიწერა ფაილში: '{filename}'")

    with open(filename, "r", encoding="utf-8") as file:
        file_content = file.readline()
    print("4. ფაილიდან წაკითხული ხაზი:", file_content)

    p2 = deserialize_person(file_content)
    print("5. დესერიალიზებული ახალი ობიექტი (p2):", p2)

    print("6. p2-ის ტიპი არის:", type(p2))