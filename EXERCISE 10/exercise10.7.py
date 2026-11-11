# Create a loop for the calculator
while True:
    print("\nEnter 'q' to quit.")

    try:
        number1 = input("Enter the first number: ")
        if number1 == 'q':
            break

        number2 = input("Enter the second number: ")
        if number2 == 'q':
            break

        result = int(number1) + int(number2)

    except ValueError:
        print("Sorry, please enter numbers only!")

    else:
        print(f"The result is: {result}")