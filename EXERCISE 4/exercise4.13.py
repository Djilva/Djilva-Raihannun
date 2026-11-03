foods = ("Fried Rice", "Chicken Soup", "Grilled Fish",
         "French Fries", "Vegetable Salad")

print("The restaurant offers the following foods:")
for food in foods:
    print(food)

print("\nTrying to change one food:")
foods[0] = "Fried Chicken"

print("\nThe restaurant's revised menu:")
foods = ("Fried Chicken", "Chicken Soup", "Grilled Fish",
         "Mashed Potatoes", "Fruit Salad")

for food in foods:
    print(food)
    
# setelah diperbaiki

foods = ("Fried Rice", "Chicken Soup", "Grilled Fish",
         "French Fries", "Vegetable Salad")

print("The restaurant offers the following foods:")
for food in foods:
    print(food)

try:
    foods[0] = "Fried Chicken"
except TypeError:
    print("\nPython does not allow changes to a tuple.")

foods = ("Fried Chicken", "Chicken Soup", "Grilled Fish",
         "Mashed Potatoes", "Fruit Salad")

print("\nThe restaurant's revised menu:")
for food in foods:
    print(food)