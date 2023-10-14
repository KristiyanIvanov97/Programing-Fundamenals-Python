first_sequence_of_strings = input().split(", ")
second_sequence_of_strings = input().split(", ")
new_list = []
for curr_str in first_sequence_of_strings:
    for string in second_sequence_of_strings:
        if curr_str in string:
            if curr_str not in new_list:
                new_list.append(curr_str)

print(new_list)

