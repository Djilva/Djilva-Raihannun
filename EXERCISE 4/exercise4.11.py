pizzas = ["Pepperoni", "Cheese", "Mushroom"]

friend_pizzas = pizzas[:]

pizzas.append("Chicken")
friend_pizzas.append("Beef")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)