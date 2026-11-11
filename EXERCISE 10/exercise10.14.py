import json
from pathlib import Path

filename = Path(__file__).with_name('username.json')


def get_new_username():
    """Ask for a new username and save it."""
    username = input("What is your name? ")

    with open(filename, 'w') as file_object:
        json.dump(username, file_object)

    return username


def greet_user():
    """Greet the user by name."""
    try:
        with open(filename) as file_object:
            username = json.load(file_object)

    except FileNotFoundError:
        username = get_new_username()

    else:
        correct = input(
            f"Are you {username}? (yes/no): "
        )

        if correct.lower() != 'yes':
            username = get_new_username()

    print(f"Welcome back, {username}!")


greet_user()