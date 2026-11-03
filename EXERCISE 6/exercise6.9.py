favorite_places = {
    "Djilva": ["London", "Switzerland", "Amsterdam"],
    "Rai": ["Tokyo", "Seoul"],
    "Hannun": ["Paris", "Istanbul", "Edinburgh"]
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")

    for place in places:
        print(f"- {place}")

    print()