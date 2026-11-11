import json

# Ask the user for their favorite number
favorite_number = input("What is your favorite number? ")

# Store the number in a file
filename = 'favorite_number.json'

with open(filename, 'w') as file_object:
    json.dump(favorite_number, file_object)

print("Your favorite number has been saved!")