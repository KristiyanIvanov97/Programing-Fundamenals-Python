shopping_list = input().split("!")
command = input()
while command != "Go Shopping!":
    new_command = command.split()

    if new_command[0] == "Urgent":
        item = new_command[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif new_command[0] == "Unnecessary":
        item = new_command[1]
        if item in shopping_list:
            shopping_list.remove(item)
    elif new_command[0] == "Correct":
        if new_command[1] in shopping_list:
            old_item = new_command[1]
            index = shopping_list.index(new_command[1])
            new_item = new_command[2]
            shopping_list[index] = new_item
    elif new_command[0] == "Rearrange":
        item = new_command[1]
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
    command = input()

print(", ".join(shopping_list))
