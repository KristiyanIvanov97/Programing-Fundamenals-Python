def characters_in_range(first, second):
    list_of_characters = []
    for current_char in range(ord(first) + 1, ord(second)):
        list_of_characters.append(chr(current_char))
    return list_of_characters


first_character = input()
second_character = input()
# print(*characters_in_range(first_character, second_character))
final_result = characters_in_range(first_character, second_character)
print(" ".join(final_result))