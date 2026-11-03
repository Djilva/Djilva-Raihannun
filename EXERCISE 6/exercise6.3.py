# Membuat dictionary yang berisi lima istilah pemrograman Python yang telah dipelajari pada bab sebelumnya
glossary = {
    "Variable": "A name used to store data in a program.",
    "List": "A collection of items stored in a single variable.",
    "Loop": "A structure used to repeat a block of code.",
    "Conditional": "A statement used to make decisions in a program.",
    "Dictionary": "A collection of key-value pairs."
}

for word, meaning in glossary.items():
    print(f"{word}:")
    print(f"    {meaning}\n")