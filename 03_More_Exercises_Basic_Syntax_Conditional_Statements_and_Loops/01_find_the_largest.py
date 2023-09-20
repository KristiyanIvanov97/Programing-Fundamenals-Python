# number = input()
#
#
# for char in number:
#
# integer = 56786
# string = str(integer)
# new_integer = 0
# for items in string:
#     new_integer = int(items)
#
# print(new_integer)

number_to_str = input()

largest_num = ""
current_max = "0"

for digit in number_to_str:
    for char in number_to_str:

        if digit > current_max:
            largest_num += digit
            current_max = digit
        else:
            largest_num += digit

largest_num = int(largest_num)

print(largest_num)