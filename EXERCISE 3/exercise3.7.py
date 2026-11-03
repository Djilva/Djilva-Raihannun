guests = ["Windi", "Kala", "Tea","Faya", "Ren", "Desy"]

print("Sorry, I can only invite two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print(f"Hello {guests[0]}, you are still invited to dinner.")
print(f"Hello {guests[1]}, you are still invited to dinner.")

del guests[0]
del guests[0]

print(guests)