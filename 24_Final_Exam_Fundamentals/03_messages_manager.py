capacity_of_messages = int(input())
messages = {}
command = input().split("=")
# messages[username][0] - sent messages , messages[username][1] - received messages
while command[0] != "Statistics":
    if command[0] == "Add":
        username = command[1]
        sent = int(command[2])
        received = int(command[3])
        if username not in messages:
            messages[username] = [sent, received]
    elif command[0] == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in messages and receiver in messages:
            messages[sender][0] += 1
            messages[receiver][1] += 1
        if messages[sender][0] + messages[sender][1] == capacity_of_messages:
            messages.pop(sender)
            print(f"{sender} reached the capacity!")
        if messages[receiver][1] + messages[receiver][0] == capacity_of_messages:
            messages.pop(receiver)
            print(f"{receiver} reached the capacity!")
    elif command[0] == "Empty":
        username = command[1]
        if username == "All":
            messages.clear()
        elif username in messages:
            messages.pop(username)
    command = input().split("=")

print(f"Users count: {len(messages)}")
for user, info in messages.items():
    print(f"{user} - {info[0] + info[1]}")
