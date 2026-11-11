import json
from pathlib import Path

# Ask the user for information
username = input("What is your name? ")
hobby = input("What is your favorite hobby? ")
subject = input("What is your favorite subject? ")

# Store the information in a dictionary
user_info = {
    'username': username,
    'hobby': hobby,
    'subject': subject
}

# Write the dictionary to a file
filename = Path(__file__).with_name('user_info.json')

with open(filename, 'w') as file_object:
    json.dump(user_info, file_object)

# Read the information from the file
with open(filename) as file_object:
    saved_info = json.load(file_object)

# Print a summary
print("\nHere's what I know about you:")
print(f"Your name is {saved_info['username']}.")
print(f"Your favorite hobby is {saved_info['hobby']}.")
print(f"Your favorite subject is {saved_info['subject']}.")