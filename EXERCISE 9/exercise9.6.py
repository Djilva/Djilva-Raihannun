class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanila", "Cokelat", "Strawberry", "Matcha", "Mangga"]

    def display_flavors(self):
        print("Pilihan rasa es krim yang tersedia:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Membuat instance dan memanggil method
my_ice_cream_stand = IceCreamStand("Es Krim Nikmat")
my_ice_cream_stand.describe_restaurant()
print()
my_ice_cream_stand.display_flavors()