activation_key = input()

command = input()

while command != "Generate":
    if command.startswith("Contains"):
        _, substring = command.split(">>>")
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command.startswith("Flip"):
        _, upper_or_lower, start_index, end_index = command.split(">>>")
        start_index = int(start_index)
        end_index = int(end_index)
        if upper_or_lower == "Upper":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper()\
                             + activation_key[end_index:]
        elif upper_or_lower == "Lower":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower()\
                             + activation_key[end_index:]
        print(activation_key)
    elif command.startswith("Slice"):
        _, start_index, end_index = command.split(">>>")
        start_index = int(start_index)
        end_index = int(end_index)
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")