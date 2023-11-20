import re

text = input()
searched_word = input()
pattern = fr"\b{searched_word}\b"

matched_words = re.findall(pattern, text, re.IGNORECASE)

print(len(matched_words))
