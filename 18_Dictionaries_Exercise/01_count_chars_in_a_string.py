some_text = [char for char in input() if char != ' ']
chars_count = {}
for char in some_text:
    if char not in chars_count.keys():
        chars_count[char] = 0
    chars_count[char] += 1

for char, occurrences in chars_count.items():
    print(f"{char} -> {occurrences}")

