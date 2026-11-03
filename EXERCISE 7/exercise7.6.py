# Menggunakan conditional test pada while statement
prompt = "Enter a pizza topping:"
prompt += "\nEnter 'quit' to finish: "

topping = ""

while topping != "quit":
    topping = input(prompt)

    if topping != "quit":
        print(f"I will add {topping} to your pizza.")

# Menggunakan active variable
prompt = "Enter a pizza topping:"
prompt += "\nEnter 'quit' to finish: "

active = True

while active:
    topping = input(prompt)

    if topping == "quit":
        active = False
    else:
        print(f"I will add {topping} to your pizza.")

# Menggunakan break statement
prompt = "Enter a pizza topping:"
prompt += "\nEnter 'quit' to finish: "

while True:
    topping = input(prompt)

    if topping == "quit":
        break

    print(f"I will add {topping} to your pizza.")