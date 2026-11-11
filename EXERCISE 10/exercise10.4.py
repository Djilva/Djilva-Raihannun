# Ask the user for their name
name = input("Please enter your name: ")

# Write the name to a file
filename = "guest.txt"

with open(filename, 'w') as file_object:
    file_object.write(name)

print(f"Welcome, {name}!")