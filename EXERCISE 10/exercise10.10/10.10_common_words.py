from pathlib import Path

filenames = ['alice.txt', 'pride.txt']

for filename in filenames:
    path = Path(__file__).with_name(filename)

    with open(path, encoding='utf-8') as file_object:
        contents = file_object.read()

    the_count = contents.lower().count('the')
    the_space_count = contents.lower().count('the ')

    print(f"\nFile: {filename}")
    print(f"The word 'the' appears {the_count} times.")
    print(f"The word 'the ' appears {the_space_count} times.")