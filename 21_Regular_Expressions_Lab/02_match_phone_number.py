import re

phone_numbers = input()

pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"

valid_phone_numbers = re.findall(pattern, phone_numbers)

print(", ".join(valid_phone_numbers))


