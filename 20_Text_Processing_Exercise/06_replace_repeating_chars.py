some_string = input()
final_string = ""
previous_char = ""
for char in some_string:
    if char != previous_char:
        final_string += char
    previous_char = char

print(final_string)
