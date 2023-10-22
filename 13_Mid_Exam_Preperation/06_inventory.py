some_items = input().split(", ")

while True:
    some_command = input()
    if some_command == "Craft!":
        break
    command = some_command.split(" - ")
    if command[0] == "Collect":
        if command[1] not in some_items:
            some_items.append(command[1])
    elif command[0] == "Drop":
        if command[1] in some_items:
            some_items.remove(command[1])
    elif command[0] == "Combine Items":
        old_item, new_item = command[1].split(":")
        if old_item in some_items:
            old_item_index = some_items.index(old_item)
            some_items.insert(old_item_index + 1, new_item)
    elif command[0] == "Renew":
        if command[1] in some_items:
            some_items.remove(command[1])
            some_items.append(command[1])

print(", ".join(some_items))
