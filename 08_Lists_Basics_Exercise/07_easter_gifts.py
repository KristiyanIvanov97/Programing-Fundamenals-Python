names_of_the_gifts = input().split()
command = input().split()
end_command = ["No", "Money"]
while command != end_command:
    if command[0] == "OutOfStock":
        index = 0
        for gift in names_of_the_gifts:
            if gift == command[1]:
                names_of_the_gifts.pop(index)
                names_of_the_gifts.insert(index, "None")
            index += 1
    elif command[0] == "Required":
        if int(command[2]) < len(names_of_the_gifts):
            names_of_the_gifts.pop(int(command[2]))
            names_of_the_gifts.insert(int(command[2]), command[1])
    elif command[0] == "JustInCase":
        names_of_the_gifts.pop()
        names_of_the_gifts.append(command[1])

    command = input().split()

for gifts in names_of_the_gifts:
    if gifts == "None":
        names_of_the_gifts.remove("None")
print(*names_of_the_gifts)
