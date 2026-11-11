filename = "learning_python.txt"

# Read the entire file
with open(filename) as file_object:
    contents = file_object.read()

print("Reading the entire file:")
print(contents)


# Read the file using a list
with open(filename) as file_object:
    lines = file_object.readlines()

print("Reading the file line by line:")

for line in lines:
    print(line.strip())