favorite_numbers = {
    "Minji": [7, 15, 21],
    "Hanni": [12, 24],
    "Danielle": [5, 10, 25],
    "Haerin": [9, 18],
    "Hyein": [3, 6, 12]
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")

    for number in numbers:
        print(number)

    print()