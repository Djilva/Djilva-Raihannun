# Membuat dua list username, yaitu current_users dan new_user
current_users = ["Windi", "Kala", "Tea", "Vrysa", "Lana"]

new_users = ["windi", "Faya", "Desy", "TEA", "Nayla"]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is already taken.")
    else:
        print(f"{new_user} is available.")