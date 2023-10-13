command = input()
notes = [0] * 10
while command != "End":
    to_do = command.split("-")
    importance = int(to_do[0]) - 1
    action = to_do[1]
    notes.pop(importance)
    notes.insert(importance, action)
    command = input()

final_list = [action for action in notes if action != 0]
print(final_list)
