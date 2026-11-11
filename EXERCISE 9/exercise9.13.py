from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        # Mengembalikan angka acak antara 1 dan jumlah sisi dadu
        return randint(1, self.sides)

# 1. Membuat dahu 6-sisi dan melemparnya 10 kali
print("--- Pelemparan Dadu 6 Sisi (10 kali) ---")
six_sided_die = Die()
results_6 = [six_sided_die.roll_die() for _ in range(10)]
print(results_6)

# 2. Membuat dadu 10-sisi dan melemparnya 10 kali
print("\n--- Pelemparan Dadu 10 Sisi (10 kali) ---")
ten_sided_die = Die(10)
results_10 = [ten_sided_die.roll_die() for _ in range(10)]
print(results_10)

# 3. Membuat dadu 20-sisi dan melemparnya 10 kali
print("\n--- Pelemparan Dadu 20 Sisi (10 kali) ---")
twenty_sided_die = Die(20)
results_20 = [twenty_sided_die.roll_die() for _ in range(10)]
print(results_20)