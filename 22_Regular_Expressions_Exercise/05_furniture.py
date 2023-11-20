import re

total_cost = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
all_furniture = []
command = input()
while command != "Purchase":
    valid_furniture = re.search(pattern, command)
    if valid_furniture:
        furniture, price, quantity = valid_furniture.groups()
        all_furniture.append(furniture)
        total_cost += int(quantity) * float(price)
    command = input()

print("Bought furniture:")
for furniture in all_furniture:
    print(furniture)

print(f"Total money spend: {total_cost:.2f}")
