prompt = "Enter a pizza topping:"
prompt += "\nEnter 'quit' to finish: "

while True:
    topping = input(prompt)

    if topping == "quit":
        break
    else:
        print(f"I will add {topping} to your pizza.")