class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!\n")

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Hak akses (Privileges) untuk Admin {self.first_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Membuat instance Admin dan memanggil method-nya
admin_user = Admin("Djilva", "Raihannun", 18, "Karnganyar")
admin_user.describe_user()
admin_user.show_privileges()