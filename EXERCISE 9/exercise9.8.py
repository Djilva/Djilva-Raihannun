class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Daftar Hak Akses (Privileges):")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        # Menjadikan class Privileges sebagai atribut
        self.privileges = Privileges()

# Membuat instance Admin baru dan memanggil method show_privileges()
admin_user = Admin("Kim", "Minji", 22, "Bandung")
admin_user.describe_user()
print()
admin_user.privileges.show_privileges()