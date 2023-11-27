encrypted_message = input()

instructions = input()
while instructions != "Decode":
    action = instructions.split("|")[0]
    if action == "Move":
        number_of_letters = int(instructions.split("|")[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif action == "Insert":
        index = int(instructions.split("|")[1])
        value = instructions.split("|")[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif action == "ChangeAll":
        substring = instructions.split("|")[1]
        replacement = instructions.split("|")[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    instructions = input()
print(f"The decrypted message is: {encrypted_message}")


