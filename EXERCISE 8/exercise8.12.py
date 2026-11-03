def make_sandwich(*items):
    print("\nYour sandwich order:")
    for item in items:
        print(f"- {item}")

    print("Your sandwich is ready to be prepared!")


make_sandwich("cheese", "tomato")

make_sandwich("chicken", "lettuce", "mayonnaise")

make_sandwich("beef", "onion", "cheese", "chili sauce")