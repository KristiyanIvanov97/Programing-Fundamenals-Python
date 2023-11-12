text = input()
letters = ""
digits = ""
other_characters = ""
for char in text:
    if char.isnumeric():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        other_characters += char

print(f"{digits}\n{letters}\n{other_characters}")


