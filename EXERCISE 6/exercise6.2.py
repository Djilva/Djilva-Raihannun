# Membuat dictionary yang menyimpan angka favorit dari lima orang. Nama digunakan sebagai key, sedangkan angka favorit digunakan sebagai value
favorite_numbers = {
    "Djilva": 23,
    "Kala": 21,
    "Tea": 7,
    "Windi": 10,
    "Faya": 18
}

print("Everyone's favorite numbers:")

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")