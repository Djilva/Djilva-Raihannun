class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("City:", self.city)

    def greet_user(self):
        print("Hello,", self.first_name, self.last_name + "!")
        print("Welcome back!")


user1 = User("Kim", "Minji", 22, "Jakarta")
user2 = User("Pham", "Hanni", 22, "Bandung")
user3 = User("Mo", "Dani", 21, "Surabaya")

user1.describe_user()
user1.greet_user()

print()

user2.describe_user()
user2.greet_user()

print()

user3.describe_user()
user3.greet_user()