# Program 8-1: Message
def display_message():
    print("I am learning Python functions.")


display_message()

# Program 8-5: Cities
def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")


describe_city("Reykjavik")
describe_city("Akureyri")
describe_city("Tokyo", "Japan")

# Program 8-12: Sandwiches
def make_sandwich(*items):
    print("\nYour sandwich order:")

    for item in items:
        print(f"- {item}")

    print("Your sandwich is ready to be prepared!")


make_sandwich("cheese", "tomato")
make_sandwich("chicken", "lettuce", "mayonnaise")
make_sandwich("beef", "onion", "cheese")