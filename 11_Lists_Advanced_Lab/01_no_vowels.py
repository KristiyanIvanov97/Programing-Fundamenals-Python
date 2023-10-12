string = input()
new_string = [curr_char for curr_char in string if curr_char.lower() not in ['a', 'o', 'u', 'e', 'i']]
# for curr_char in string:
#     if curr_char.lower() not in ['a', 'o', 'u', 'e', 'i']:
#         new_string.append(curr_char)

print("".join(new_string))
