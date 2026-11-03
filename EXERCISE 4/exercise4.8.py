# Membuat list berisi 10 angka pertama yang sudah dipangkatkan tiga (kubik), kemudian menggunakan for loop untuk menampilkan hasilnya
cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)