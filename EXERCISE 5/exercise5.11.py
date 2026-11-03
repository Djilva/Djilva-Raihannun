# Membuat list berisi angka 1 sampai 9. Kemudian menggunakan for loop dan if-elif-else untuk menampilkan angka dengan akhiran ordinal yang benar, seperti 1st, 2nd, dan 3rd
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")