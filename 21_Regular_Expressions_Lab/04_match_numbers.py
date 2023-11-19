import re

text = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

matched_numbers = re.finditer(pattern, text)

for match in matched_numbers:
    print(match.group(), end=" ")

