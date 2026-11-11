import json

# Read the favorite number from the file
filename = 'favorite_number.json'

with open(filename) as file_object:
    favorite_number = json.load(file_object)

print(f"I know your favorite number! It's {favorite_number}.")