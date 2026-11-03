person_1 = {
    "first_name": "Djilva",
    "last_name": "Raihannun",
    "age": 18,
    "city": "Karanganyar"
}

person_2 = {
    "first_name": "Kim",
    "last_name": "Minji",
    "age": 22,
    "city": "Bandung"
}

person_3 = {
    "first_name": "Pham",
    "last_name": "Hanni",
    "age": 22,
    "city": "Surabaya"
}

people = [person_1, person_2, person_3]

for person in people:
    print("Person Information:")
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()