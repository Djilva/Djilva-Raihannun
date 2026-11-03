pet_1 = {
    "animal": "Dog",
    "owner": "Hanni",
    "age": 3,
    "favorite_food": "Chicken"
}

pet_2 = {
    "animal": "Cat",
    "owner": "Djilva",
    "age": 2,
    "favorite_food": "Fish"
}

pet_3 = {
    "animal": "Rabbit",
    "owner": "Minji",
    "age": 1,
    "favorite_food": "Carrot"
}

pets = [pet_1, pet_2, pet_3]

print("PET INFORMATION")
print("----------------")

for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print(f"Age: {pet['age']} years old")
    print(f"Favorite Food: {pet['favorite_food']}")
    print()