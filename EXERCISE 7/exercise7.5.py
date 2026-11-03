prompt = "Enter your age:"
prompt += "\nEnter 0 to finish: "

while True:
    age = int(input(prompt))

    if age == 0:
        break
    elif age < 3:
        print("Your movie ticket is free.")
    elif age <= 12:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")