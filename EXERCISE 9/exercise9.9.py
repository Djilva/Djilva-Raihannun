class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range_miles = 260
        elif self.battery_size == 65:
            range_miles = 220
        elif self.battery_size > 75:
            range_miles = 315
        else:
            range_miles = 0
            
        print(f"This car can go about {range_miles} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 75:
            self.battery_size = 75
            print("Baterai telah ditingkatkan menjadi 75 kWh.")
        else:
            print("Baterai sudah memiliki kapasitas maksimal (75 kWh).")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(65)  # Mulai dengan baterai default 65 kWh

# Pengujian kode:
my_tesla = ElectricCar("tesla", "model s", 2024)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
print("Jarak tempuh awal:")
my_tesla.battery.get_range()

print("\nMelakukan upgrade baterai...")
my_tesla.battery.upgrade_battery()

print("Jarak tempuh setelah di-upgrade:")
my_tesla.battery.get_range()