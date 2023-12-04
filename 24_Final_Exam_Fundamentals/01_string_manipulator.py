some_string = input()

command = input().split()

while command[0] != "End":
    if command[0] == "Translate":
        char = command[1]
        replacement = command[2]
        some_string = some_string.replace(char, replacement)
        print(some_string)
    elif command[0] == "Includes":
        substring = command[1]
        if substring in some_string:
            print("True")
        else:
            print("False")
    elif command[0] == "Start":
        substring = command[1]
        if some_string.startswith(substring):
            print("True")
        else:
            print("False")
    elif command[0] == "Lowercase":
        some_string = some_string.lower()
        print(some_string)
    elif command[0] == "FindIndex":
        char = command[1]
        current_index = some_string.rfind(char)
        print(current_index)
    elif command[0] == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        some_string = some_string[:start_index] + some_string[start_index + count:]
        print(some_string)
    command = input().split()

