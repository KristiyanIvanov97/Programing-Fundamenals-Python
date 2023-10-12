number_of_wagons = int(input())
train = []
for _ in range(number_of_wagons):
    train.append(0)

command = input()

while command != "End":
    new_command = command.split()
    if new_command[0] == "add":
        train[-1] += int(new_command[1])
    elif new_command[0] == "insert":
        train[int(new_command[1])] += int(new_command[2])
    elif new_command[0] == "leave":
        train[int(new_command[1])] -= int(new_command[2])

    command = input()
print(train)


