products = {}
while True:
    command = input()
    if command == "statistics":
        break

    elements = command.split(": ")
    for index in range(0, len(elements), 2):
        product = elements[index]
        quantity = int(elements[index + 1])
        if product not in products:
            products[product] = 0
        products[product] += quantity

print("Products in stock:")
for product in products:
    print(f"- {product}: {products[product]}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
