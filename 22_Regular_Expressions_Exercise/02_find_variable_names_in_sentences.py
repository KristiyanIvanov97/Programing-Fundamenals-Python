import re

text = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
valid_names = re.findall(pattern, text)
print(",".join(valid_names))
