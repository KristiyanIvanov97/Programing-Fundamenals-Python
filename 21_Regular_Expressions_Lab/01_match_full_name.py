import re

name = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
valid_names = re.findall(pattern, name)

print(" ".join(valid_names))


