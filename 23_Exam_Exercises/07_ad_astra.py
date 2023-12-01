import re

some_string = input()
total_calories = 0

pattern = r"([#|])([A-Za-z\s]+)(\1)(\d{2}/\d{2}/\d{2})(\1)(\d+)(\1)"

matches = re.findall(pattern, some_string)

for match in matches:
    total_calories += int(match[5])

print(f"You have food to last you for: {total_calories // 2000} days!")

for match in matches:
    print(f"Item: {match[1]}, Best before: {match[3]}, Nutrition: {match[5]}")
