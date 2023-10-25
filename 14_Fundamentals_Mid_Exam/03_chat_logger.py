messages = []

while True:
    command = input().split()
    action = command[0]
    if action == "Chat":
        message = command[1]
        messages.append(message)
    elif action == "Delete":
        message = command[1]
        if message in messages:
            messages.remove(message)
    elif action == "Edit":
        message = command[1]
        new_message = command[2]
        if message in messages:
            old_message_index = messages.index(message)
            messages[old_message_index] = new_message
    elif action == "Pin":
        message = command[1]
        if message in messages:
            messages.remove(message)
            messages.append(message)
    elif action == "Spam":
        for curr_spam in command:
            if curr_spam != "Spam":
                messages.append(curr_spam)
    elif action == "end":
        break

print("\n".join(messages))
