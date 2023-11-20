import re

string = input()

while string:
    pattern = r"\d+"
    numbers = re.findall(pattern, string)
    if numbers:
        print(" ".join(numbers), end=" ")
    string = input()
