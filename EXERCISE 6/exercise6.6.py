favorite_languages = {
    "Djilva": "Python",
    "Rai": "Java",
    "Hannun": "C++",
    "Raihannun": "Python"
}

people = ["Djilva", "Rai", "Minji", "Hannun", "Hanni", "Raihannun"]

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person}, for taking the poll!")
    else:
        print(f"{person}, please take our favorite languages poll.")