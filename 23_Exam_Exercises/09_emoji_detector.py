import re
text = input()
digits_pattern = r"\d"
all_digits = re.findall(digits_pattern, text)
cool_threshold_sum = 1
for digit in all_digits:
    cool_threshold_sum *= int(digit)
emoji_pattern = r"(\*{2}|:{2})([A-Z][a-z]{2,})(\1)"
matches = re.findall(emoji_pattern, text)

cool_emojis = []
for match in matches:
    current_emoji_value = 0
    for char in match[1]:
        current_emoji_value += ord(char)
    if current_emoji_value > cool_threshold_sum:
        cool_emojis.append(match)

print(f"Cool threshold: {cool_threshold_sum}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print("".join(emoji))
