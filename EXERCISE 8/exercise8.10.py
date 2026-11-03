def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()

        print(current_message)
        sent_messages.append(current_message)


messages = [
    "Have a nice day!",
    "Keep learning Python!",
    "Never give up!",
    "Believe in yourself!"
]

sent_messages = []

send_messages(messages[:], sent_messages)

print("\nOriginal messages:")
print(messages)

print("\nSent messages:")
print(sent_messages)