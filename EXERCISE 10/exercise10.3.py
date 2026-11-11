# Membaca isi file
with open('learning_python.txt') as file_object:
    contents = file_object.read()

# Melakukan perulangan langsung menggunakan splitlines()
for line in contents.splitlines():
    modified_line = line.replace('Python', 'C')
    print(modified_line)