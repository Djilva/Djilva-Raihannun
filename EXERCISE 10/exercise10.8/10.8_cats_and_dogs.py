from pathlib import Path

# Define the file names
filenames = ['cats.txt', 'dogs.txt']

# Read each file
for filename in filenames:
    try:
        path = Path(__file__).with_name(filename)

        with open(path) as file_object:
            contents = file_object.read()

        print(f"\nContents of {filename}:")
        print(contents)

    except FileNotFoundError:
        print(f"Sorry, the file {filename} was not found.")