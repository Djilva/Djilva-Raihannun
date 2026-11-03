# Membuat pengujian kondisi tambahan menggunakan beberapa jenis perbandingan
# Tests for equality and inequality with strings
food = "Pizza"

print(food == "Pizza")
print(food != "Burger")

# Tests using the lower() method
name = "ANDI"

print(name.lower() == "andi")
print(name.lower() == "budi")

# Numerical tests
number = 15

print(number == 15)
print(number != 15)
print(number > 10)
print(number < 10)
print(number >= 15)
print(number <= 10)

# Tests using and and or
age = 20

print(age > 15 and age < 25)
print(age < 15 or age > 25)

# Test whether an item is in a list
animals = ["Dog", "Cat", "Rabbit"]

print("Cat" in animals)
print("Tiger" in animals)

# Test whether an item is not in a list
print("Lion" not in animals)
print("Dog" not in animals)