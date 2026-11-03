# Memperbaiki program 6.3 dengan menggunakan for loop untuk menampilkan seluruh istilah dan artinya
glossary = {
    "Variable": "A name used to store data.",
    "List": "A collection of items in one variable.",
    "Loop": "A structure used to repeat code.",
    "Conditional": "A statement used to make decisions.",
    "Dictionary": "A collection of key-value pairs.",
    "Tuple": "A collection of items that cannot be changed.",
    "String": "A sequence of characters.",
    "Integer": "A whole number.",
    "Boolean": "A data type with True or False values.",
    "Function": "A reusable block of code."
}

for word, meaning in glossary.items():
    print(f"{word}:")
    print(f"    {meaning}\n")