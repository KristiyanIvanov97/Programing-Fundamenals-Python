import re
some_string = input()
pattern = r"(@|#)+([a-z]{3,}\b)(\1?)([^a-zA-Z]+[^0-9])?(\/)(\d+)(\/+)"

valid_eggs = re.findall(pattern, some_string)

for egg in valid_eggs:
    print(f"You found {egg[5]} {egg[1]} eggs!")
