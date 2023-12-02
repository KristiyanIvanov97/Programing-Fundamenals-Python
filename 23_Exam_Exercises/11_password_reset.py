password = input()
command = input().split(" ")

while command[0] != "Done":
    if command[0] == "TakeOdd":
        new_password = ""
        for i in range(len(password)):
            if i % 2 != 0:
                new_password += password[i]
        password = new_password
        print(password)
    elif command[0] == "Cut":
        start_index = int(command[1])
        length = int(command[2])
        password = password[:start_index] + password[start_index + length:]
        print(password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input().split(" ")

print(f"Your password is: {password}")
