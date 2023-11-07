dict_of_products = {}
products_price = {}
while True:
    command = input()
    if command == "buy":
        break
    products = command.split()
    product_name = products[0]
    product_price = float(products[1])
    quantity = int(products[2])
    if product_name not in dict_of_products:
        dict_of_products[product_name] = 0
    dict_of_products[product_name] += quantity
    products_price[product_name] = product_price


for product_name, quantity in dict_of_products.items():
    total_price = quantity * products_price[product_name]
    print(f"{product_name} -> {total_price:.2f}")

