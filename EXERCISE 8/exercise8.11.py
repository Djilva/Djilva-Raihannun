def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()

        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


messages = [
    "Good morning!",
    "Study hard!",
    "Stay positive!",
    "Have a great day!"
]

sent_messages = []

send_messages(messages[:], sent_messages)

print("\nOriginal list:")
print(messages)

print("\nSent messages:")
print(sent_messages)