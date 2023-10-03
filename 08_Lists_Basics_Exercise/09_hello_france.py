items_for_buying = input()
budget = float(input())
bought_items = []
profit = 0
total_sum = 0
items = items_for_buying.split("|")

for current_item in items:
    item_type, price = current_item.split("->")
    price = float(price)
    if price <= budget:
        if item_type == "Clothes" and price <= 50:
            profit += price * 1.4 - price
            budget -= price
            bought_items.append(format(price * 1.4, ".2f"))
        elif item_type == "Shoes" and price <= 35:
            profit += price * 1.4 - price
            budget -= price
            bought_items.append(format(price * 1.4, ".2f"))
        elif item_type == "Accessories" and price <= 20.50:
            profit += price * 1.4 - price
            budget -= price
            bought_items.append(format(price * 1.4, ".2f"))

print(*bought_items)
print(f"Profit: {profit:.2f}")

for item in bought_items:
    total_sum += float(item)

if total_sum + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
