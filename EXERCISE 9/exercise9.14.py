from random import choice

# Daftar berisi 10 angka dan 5 huruf
lottery_pool = (1, 3, 7, 12, 15, 22, 27, 34, 42, 50, 'a', 'b', 'c', 'd', 'e')

# Memilih 4 item secara acak tanpa duplikasi menggunakan choice berulang atau sample
winning_ticket = []
while len(winning_ticket) < 4:
    picked = choice(lottery_pool)
    if picked not in winning_ticket:
        winning_ticket.append(picked)

print("--- Hasil Undian Lotere ---")
print(f"Kombinasi pemenang: {winning_ticket}")
print("Pesan: Tiket apa pun yang mencocokkan 4 angka atau huruf ini memenangkan hadiah!")