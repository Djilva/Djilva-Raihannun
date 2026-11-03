# Membuat list berisi minimal lima username, termasuk admin
usernames = ["admin", "windi", "kala", "tea", "vrysa"]

for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to check the latest updates?")
    else:
        print(f"Hello {username}, welcome back to your account.")