number_of_orders = int(input())
total_price = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if capsules_per_day < 1 or days < 1 \
            or days > 31 \
            or price_per_capsule < 0.01 \
            or price_per_capsule > 100 \
            or capsules_per_day > 2000:
        continue
    price_for_order = days * capsules_per_day * price_per_capsule
    print(f"The price for the coffee is: ${price_for_order:.2f}")
    total_price += price_for_order

print(f"Total: ${total_price:.2f}")

