contacts = {}
while True:
    command = input()
    if "-" not in command:
        break
    name, phone_number = command.split("-")
    contacts[name] = phone_number

searches = int(command)
for call in range(searches):
    searched_person = input()

    if searched_person in contacts.keys():
        print(f"{searched_person} -> {contacts[searched_person]}")
    else:
        print(f"Contact {searched_person} does not exist.")
