from random import choice

def get_winning_ticket(pool):
    """Menghasilkan kombinasi 4 angka/huruf acak."""
    winning = []
    while len(winning) < 4:
        picked = choice(pool)
        if picked not in winning:
            winning.append(picked)
    return winning

def check_ticket(played_ticket, winning_ticket):
    """Mengecek apakah semua elemen di played_ticket ada di winning_ticket (tanpa peduli urutan)."""
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    return True

# Kumpulan elemen undian
lottery_pool = (1, 3, 7, 12, 15, 22, 27, 34, 42, 50, 'a', 'b', 'c', 'd', 'e')

# Tiket pilihan kamu
my_ticket = (7, 15, 'a', 'd')

plays = 0
won = False

# Loop berjalan sampai tiket kamu menang
while not won:
    new_winning_ticket = get_winning_ticket(lottery_pool)
    plays += 1
    
    # Cek apakah tiket cocok
    if check_ticket(my_ticket, new_winning_ticket):
        won = True

print(f"--- Analisis Lotere ---")
print(f"Tiket saya: {my_ticket}")
print(f"Berhasil menang setelah diundi sebanyak: {plays:,} kali percobaan!")