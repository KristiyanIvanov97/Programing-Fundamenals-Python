some_string = input().split()
products = {}
for index in range(0, len(some_string), 2):
    product = some_string[index]
    quantity = int(some_string[index + 1])
    products[product] = quantity

print(products)
