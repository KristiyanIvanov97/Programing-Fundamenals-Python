import re

text = input()

pattern = r"(#|@)([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)"
# [1] = first_word , [4] = second_word
hidden_words = re.findall(pattern, text)
mirror_pairs = []

for match in hidden_words:
    if match[1] == match[4][::-1]:
        mirror_pairs.append(f"{match[1]} <=> {match[4]}")

if not hidden_words:
    print("No word pairs found!")
else:
    print(f"{len(hidden_words)} word pairs found!")
if not mirror_pairs:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(*mirror_pairs, sep=", ")
