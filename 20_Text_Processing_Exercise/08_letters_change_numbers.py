some_strings = [string.strip() for string in input().split()]
total_sum = 0
number = ""
for string in some_strings:
    for place in range(1, len(string) - 1):
        number += string[place]

    number = float(number)
    if string[0].isupper():
        divider = ord(string[0].lower()) - 96
        number /= divider
    else:
        multiplier = ord(string[0].lower()) - 96
        number *= multiplier

    if string[-1].isupper():
        subtract_number = ord(string[-1].lower()) - 96
        number -= subtract_number
    else:
        add_number = ord(string[-1].lower()) - 96
        number += add_number
    total_sum += number
    number = ""

print(f"{total_sum:.2f}")
