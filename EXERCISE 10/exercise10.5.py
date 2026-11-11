# Create an empty list
guest_names = []

# Ask users for their names
while True:
    name = input("Please enter your name (or 'quit' to finish): ")

    if name == 'quit':
        break

    print(f"Hello, {name}! You have been added to the guest book.")
    guest_names.append(name)

# Write all names to a file
with open('guest_book.txt', 'w') as file_object:
    for name in guest_names:
        file_object.write(name + '\n')

print("Guest book has been created!")