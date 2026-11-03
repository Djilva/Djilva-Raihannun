pet_1 = {
    "animal": "Dog",
    "owner": "Hanni"
}

pet_2 = {
    "animal": "Cat",
    "owner": "Djilva"
}

pet_3 = {
    "animal": "Rabbit",
    "owner": "Minji"
}

pet_4 = {
    "animal": "Bird",
    "owner": "Haerin"
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print("Pet Information:")
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print()