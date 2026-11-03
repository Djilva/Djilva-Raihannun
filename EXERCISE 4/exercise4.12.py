my_foods = ["Pizza", "Burger", "Fried Rice", "Noodles"]

friend_foods = my_foods[:]

my_foods.append("Spaghetti")
friend_foods.append("Sandwich")

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)