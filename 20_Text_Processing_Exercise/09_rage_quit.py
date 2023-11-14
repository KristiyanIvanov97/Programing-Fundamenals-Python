text = input()
current_string = ""
repetitions = ""
final_string = ""
for index in range(len(text)):
    if not text[index].isnumeric():
        current_string += text[index].upper()
    else:
        for next_symbol in range(index, len(text)):
            if not text[next_symbol].isdigit():
                break
            repetitions += text[next_symbol]

        final_string += current_string * int(repetitions)
        repetitions = ""
        current_string = ""

print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)
