# Program 1 - Exercise 4.1
pizzas = ["Pepperoni", "Cheese", "Mushroom"]

for pizza in pizzas:
    print(f"{pizza} pizza is one of my favorite foods.")

print("\nPizza is always a good choice for me!")

# Program 2 – Exercise 4.2
animals = ["Dog", "Cat", "Rabbit"]

for animal in animals:
    print(f"{animal} is a cute and friendly animal.")

print("\nThese animals are lovely companions to have at home!")

# Program 3 – Exercise 4.13
foods = (
    "Fried Rice",
    "Chicken Soup",
    "Grilled Fish",
    "French Fries",
    "Vegetable Salad"
)

print("The restaurant offers the following foods:")

for food in foods:
    print(food)

try:
    foods[0] = "Fried Chicken"
except TypeError:
    print("\nPython does not allow changes to a tuple.")

foods = (
    "Fried Chicken",
    "Chicken Soup",
    "Grilled Fish",
    "Mashed Potatoes",
    "Fruit Salad"
)

print("\nThe restaurant's revised menu:")

for food in foods:
    print(food)