# Menambahkan kondisi untuk memastikan list username tidak kosong
usernames = ["admin", "windi", "kala", "tea", "vrysa"]

if usernames:
    for username in usernames:
        print(f"Hello {username}, welcome back!")
else:
    print("We need to find some users!")

usernames = []

if usernames:
    for username in usernames:
        print(f"Hello {username}, welcome back!")
else:
    print("We need to find some users!")