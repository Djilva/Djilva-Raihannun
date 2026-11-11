import json

filename = 'favorite_number.json'

try:
    # Try to read the saved favorite number
    with open(filename) as file_object:
        favorite_number = json.load(file_object)

except FileNotFoundError:
    # Ask the user for their favorite number
    favorite_number = input("What is your favorite number? ")

    # Save the favorite number
    with open(filename, 'w') as file_object:
        json.dump(favorite_number, file_object)

    print("Your favorite number has been saved!")

else:
    print(f"I know your favorite number! It's {favorite_number}.")