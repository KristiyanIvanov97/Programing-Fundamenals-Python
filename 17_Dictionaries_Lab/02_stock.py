some_string = input().split()
products = {}
for index in range(0, len(some_string), 2):
    product = some_string[index]
    quantity = int(some_string[index + 1])
    products[product] = quantity

searched_products = input().split()

for curr_product in searched_products:
    if curr_product in products.keys():
        print(f"We have {products[curr_product]} of {curr_product} left")
    else:
        print(f"Sorry, we don't have {curr_product}")

